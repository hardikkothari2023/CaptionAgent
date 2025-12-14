import whisper 

def transcribe_audio(file_path):
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    print("Transcription:")
    print(result["text"])
    return result["text"]
if __name__ == "__main__":
    audio_file = "Audio/sample_audio.wav"  # Replace with your audio file path
    transcribe_audio(audio_file) 