from moviepy.editor import VideoFileClip
import os
def extract_audio_from_video(video_path, output_audio_path):
    try: 
        video = VideoFileClip(video_path)
        audio = video.audio
        if audio:
            audio.write_audiofile(output_audio_path)
            print(f"Audio extracted and saved to {output_audio_path}")
        else:
            print("No audio track found in the video.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    video_file = "Video/sample_video.mp4"  # Replace with your video file path
    output_audio_file = "Audio/sample_audio.wav"  # Desired output audio file path
    extract_audio_from_video(video_file, output_audio_file)

    os.makedirs(os.path.dirname(output_audio_file), exist_ok=True)