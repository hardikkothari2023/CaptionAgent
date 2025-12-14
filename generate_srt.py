import whisper
import srt
import json
from datetime import timedelta


def transcribe(audio_path, model_name="base"):
    """Transcribe audio with word-level timing using Whisper."""
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_path)
    return result


def convert_to_srt(transcript_result, word_level=False):
    """Convert Whisper transcription to SRT format.
    
    If word_level=True, creates one subtitle per word with individual timing.
    If word_level=False, creates one subtitle per segment.
    """
    segments = transcript_result['segments']
    subtitles = []
    
    if word_level:
        # Word-level subtitles (karaoke style)
        subtitle_index = 1
        for seg in segments:
            # Extract word-level timing if available
            if 'words' in seg:
                for word_info in seg['words']:
                    subtitle = srt.Subtitle(
                        index=subtitle_index,
                        start=timedelta(seconds=word_info['start']),
                        end=timedelta(seconds=word_info['end']),
                        content=word_info['word'].strip()
                    )
                    subtitles.append(subtitle)
                    subtitle_index += 1
            else:
                # Fallback to segment if words not available
                subtitle = srt.Subtitle(
                    index=subtitle_index,
                    start=timedelta(seconds=seg['start']),
                    end=timedelta(seconds=seg['end']),
                    content=seg['text'].strip()
                )
                subtitles.append(subtitle)
                subtitle_index += 1
    else:
        # Segment-level subtitles (standard)
        for i, seg in enumerate(segments):
            subtitle = srt.Subtitle(
                index=i + 1,
                start=timedelta(seconds=seg['start']),
                end=timedelta(seconds=seg['end']),
                content=seg['text'].strip()
            )
            subtitles.append(subtitle)
    
    return srt.compose(subtitles)


def extract_word_timing(transcript_result):
    """Extract word-level timing data for advanced processing.
    
    Returns a list of words with their start/end times.
    """
    words_with_timing = []
    segments = transcript_result['segments']
    
    for seg in segments:
        if 'words' in seg:
            for word_info in seg['words']:
                words_with_timing.append({
                    'word': word_info['word'].strip(),
                    'start': word_info['start'],
                    'end': word_info['end'],
                    'confidence': word_info.get('probability', 1.0)
                })
    
    return words_with_timing


def save_word_timing_json(words_data, output_path):
    """Save word timing data to JSON for use in video rendering."""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(words_data, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    audio_file = "Audio/sample_audio.wav"  # Replace with your audio file path
    
    # Transcribe with word-level detail
    transcript_result = transcribe(audio_file)
    
    # Generate segment-level SRT
    srt_content_segments = convert_to_srt(transcript_result, word_level=False)
    with open("captions/output_captions.srt", "w", encoding="utf-8") as srt_file:
        srt_file.write(srt_content_segments)
    print("✅ Segment-level SRT file generated")
    
    # Generate word-level SRT (for karaoke style)
    srt_content_words = convert_to_srt(transcript_result, word_level=True)
    with open("captions/output_captions_words.srt", "w", encoding="utf-8") as srt_file:
        srt_file.write(srt_content_words)
    print("✅ Word-level SRT file generated")
    
    # Extract and save word timing data
    words_data = extract_word_timing(transcript_result)
    save_word_timing_json(words_data, "captions/word_timing.json")
    print("✅ Word timing JSON generated")
    
    # Print transcript
    print("\n📝 Full Transcript:")
    print(transcript_result['text'])
    