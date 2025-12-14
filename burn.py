import os
os.environ["IMAGEMAGICK_BINARY"] = r"C:\Program Files\ImageMagick-7.1.2-Q16-HDRI\magick.exe"

from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import pysrt
import json


def srt_time_to_seconds(t):
    """Convert SRT time to seconds."""
    return (
        t.hours * 3600 +
        t.minutes * 60 +
        t.seconds +
        t.milliseconds / 1000
    )


def burn_subtitles_into_video(video_path, srt_path, output_path, fontsize=28, color="white", bg_color="black"):
    """Burn segment-level subtitles into video (standard karaoke effect)."""
    video_full = os.path.abspath(video_path)
    srt_full = os.path.abspath(srt_path)
    output_full = os.path.abspath(output_path)

    if not os.path.exists(video_full):
        raise FileNotFoundError(f"Video file not found: {video_full}")
    if not os.path.exists(srt_full):
        raise FileNotFoundError(f"SRT file not found: {srt_full}")

    video = VideoFileClip(video_full)
    subs = pysrt.open(srt_full)

    text_clips = []

    for sub in subs:
        start_time = srt_time_to_seconds(sub.start)
        end_time = srt_time_to_seconds(sub.end)

        txt_clip = TextClip(
            sub.text,
            fontsize=fontsize,
            font="Arial",
            color=color,
            bg_color=bg_color,
            method="caption",
            size=(video.w - 40, None)
        )

        txt_clip = (
            txt_clip
            .set_position(("center", "bottom"))
            .set_start(start_time)
            .set_duration(end_time - start_time)
        )

        text_clips.append(txt_clip)

    final_video = CompositeVideoClip([video] + text_clips)

    final_video.write_videofile(
        output_full,
        codec="libx264",
        audio_codec="aac",
        verbose=False,
        logger=None
    )

    video.close()
    final_video.close()


def burn_word_level_subtitles(video_path, word_timing_json, output_path, fontsize=32, 
                               text_color="white", highlight_color="yellow", bg_color="black",
                               show_next_words=3):
    """Burn word-level subtitles with karaoke effect (words highlight as spoken).
    
    Args:
        video_path: Path to input video
        word_timing_json: Path to JSON file with word timing data
        output_path: Path to output video
        fontsize: Font size for subtitles
        text_color: Color of regular words
        highlight_color: Color of currently speaking word
        bg_color: Background color for text
        show_next_words: Number of upcoming words to show in dim color
    """
    video_full = os.path.abspath(video_path)
    json_full = os.path.abspath(word_timing_json)
    output_full = os.path.abspath(output_path)

    if not os.path.exists(video_full):
        raise FileNotFoundError(f"Video file not found: {video_full}")
    if not os.path.exists(json_full):
        raise FileNotFoundError(f"Word timing JSON not found: {json_full}")

    # Load word timing data
    with open(json_full, 'r', encoding='utf-8') as f:
        words_data = json.load(f)

    video = VideoFileClip(video_full)
    text_clips = []

    # Create text clips for each word with highlighting effect
    for idx, word_info in enumerate(words_data):
        word = word_info['word']
        start_time = word_info['start']
        end_time = word_info['end']
        
        # Build display text with current word highlighted and next words visible
        display_words = []
        
        # Add previous words (faded)
        if idx > 0:
            prev_words = ' '.join([w['word'] for w in words_data[max(0, idx-2):idx]])
            if prev_words:
                display_words.append(f"<font color='gray'>{prev_words}</font>")
        
        # Add current word (highlighted)
        display_words.append(f"<font color='{highlight_color}'><b>{word}</b></font>")
        
        # Add next words (dimmed preview)
        if idx < len(words_data) - 1:
            next_end_idx = min(idx + show_next_words, len(words_data))
            next_words = ' '.join([w['word'] for w in words_data[idx+1:next_end_idx]])
            if next_words:
                display_words.append(f"<font color='gray'>{next_words}</font>")
        
        display_text = ' '.join(display_words)
        
        # Create text clip
        txt_clip = TextClip(
            display_text,
            fontsize=fontsize,
            font="Arial",
            color=text_color,
            method="caption",
            size=(video.w - 40, None)
        )
        
        txt_clip = (
            txt_clip
            .set_position(("center", "bottom"))
            .set_start(start_time)
            .set_duration(end_time - start_time)
        )
        
        text_clips.append(txt_clip)

    # Combine video with text clips
    final_video = CompositeVideoClip([video] + text_clips)

    final_video.write_videofile(
        output_full,
        codec="libx264",
        audio_codec="aac",
        verbose=False,
        logger=None
    )

    video.close()
    final_video.close()
    print(f"✅ Word-level subtitles burned successfully: {output_full}")


if __name__ == "__main__":
    # Segment-level subtitles (standard)
    burn_subtitles_into_video(
        "Video/sample_video.mp4",
        "captions/output_captions.srt",
        "Video/output_burned.mp4"
    )
    print("✅ Segment-level subtitles burned successfully")
    
    # Word-level subtitles (karaoke style) - if word timing available
    try:
        burn_word_level_subtitles(
            "Video/sample_video.mp4",
            "captions/word_timing.json",
            "Video/output_burned_words.mp4"
        )
    except FileNotFoundError as e:
        print(f"⚠️ Word-level burning skipped: {e}")
