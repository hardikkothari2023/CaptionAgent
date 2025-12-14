# 🎬 Video Caption Generator

An AI-powered web application that automatically generates captions for videos with word-level synchronization and karaoke-style effects.

## Features

✨ **Core Features:**
- 📤 Easy video upload (MP4, AVI, MOV, MKV, FLV, WMV)
- 🎙️ Automatic audio extraction using MoviePy
- 🤖 AI transcription with OpenAI Whisper
- 📝 Automatic SRT subtitle generation
- 🎨 Word-level subtitle synchronization
- ⚡ Karaoke-style subtitle effects (words highlight as spoken)
- 💾 Multiple download formats (MP4, SRT, JSON timing data)
- ⚙️ Configurable subtitle styling (font, color, position)
- 🎛️ Multiple Whisper model options (tiny to large)

## System Requirements

- **Python:** 3.8 or higher
- **ImageMagick:** Required for text rendering
- **FFmpeg:** Required for video processing
- **RAM:** 4GB minimum (8GB+ recommended for larger models)
- **GPU:** Optional but recommended for faster processing

### Install ImageMagick (Windows)

1. Download from: https://imagemagick.org/download/binaries/ImageMagick-7.1.2-Q16-HDRI-x64-dll.exe
2. Run the installer and remember the installation path
3. Update the path in `burn.py` if different from `C:\Program Files\ImageMagick-7.1.2-Q16-HDRI\magick.exe`

### Install FFmpeg (Windows)

1. Download from: https://ffmpeg.org/download.html
2. Extract and add to system PATH
3. Or install via conda: `conda install ffmpeg`

## Installation

### Option 1: Using pip (Recommended)

```bash
# Clone or navigate to the project directory
cd "d:\Project 7 sem\Video_Caption_Generater"

# Create a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install ffmpeg if not already installed
pip install ffmpeg-python
```

### Option 2: Using Conda

```bash
conda create -n video-caption python=3.10
conda activate video-caption
pip install -r requirements.txt
conda install ffmpeg
```

## Usage

### Run Streamlit App

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

### Web Interface

1. **📤 Upload & Process Tab:**
   - Select a Whisper model (tiny/base/small/medium/large)
   - Configure subtitle styling (font size, colors)
   - Upload your video file
   - Click "Start Processing"

2. **📝 Transcript Tab:**
   - View the full AI-generated transcript
   - Download as .txt file
   - See word/character statistics

3. **📌 Subtitles Tab:**
   - Preview SRT subtitle format
   - View word-level timing data
   - See timing statistics
   - Download SRT or JSON timing file

4. **📥 Downloads Tab:**
   - Download final video with embedded captions
   - Download SRT subtitle file
   - Download word-level timing data (JSON)

## Project Structure

```
Video_Caption_Generater/
├── app.py                      # Main Streamlit application
├── extract_audio.py            # Audio extraction module
├── transcribe_audio.py         # Basic transcription (optional)
├── generate_srt.py             # SRT generation with word-level timing
├── burn.py                     # Video subtitle burning (segment & word-level)
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── Video/                      # Input/output video folder
├── Audio/                      # Extracted audio files
└── captions/                   # Generated subtitle files
```

## Module Descriptions

### `app.py` - Streamlit Web Interface
- Complete UI for video processing
- Progress tracking and status updates
- Transcript, subtitle, and file download management
- Configuration sidebar for model and styling options

### `generate_srt.py` - Subtitle Generation
- **`transcribe(audio_path, model_name)`** - Transcribe audio with Whisper
- **`convert_to_srt(result, word_level)`** - Generate SRT from transcription
- **`extract_word_timing(result)`** - Extract word-level timing data
- **`save_word_timing_json(data, path)`** - Save timing data to JSON

### `burn.py` - Video Processing
- **`burn_subtitles_into_video()`** - Standard subtitle burning (segment-level)
- **`burn_word_level_subtitles()`** - Karaoke-style word-by-word subtitles
- **`srt_time_to_seconds()`** - Time conversion utility

### `extract_audio.py` - Audio Extraction
- **`extract_audio_from_video()`** - Extract audio track to WAV format

## Whisper Models

| Model  | Size  | Speed | Accuracy | Memory |
|--------|-------|-------|----------|--------|
| tiny   | 39M   | ⚡⚡⚡⚡⚡ | ⭐⭐     | ~1GB   |
| base   | 140M  | ⚡⚡⚡⚡   | ⭐⭐⭐⭐ | ~2GB   |
| small  | 244M  | ⚡⚡⚡    | ⭐⭐⭐⭐⭐| ~3GB   |
| medium | 769M  | ⚡⚡    | ⭐⭐⭐⭐⭐| ~5GB   |
| large  | 1550M | ⚡     | ⭐⭐⭐⭐⭐| ~10GB  |

## Subtitle Styling Options

### Font Size
- Range: 16-48 pixels
- Default: 28px
- Larger sizes are more readable for videos with small screens

### Text Colors
- White (default) - Best for dark backgrounds
- Custom color picker available
- Recommended: Bright colors on dark backgrounds

### Background Colors
- **Black** - Classic look, highest contrast
- **White** - For light/bright videos
- **Transparent** - Minimal, modern look
- **Semi-transparent** - Balanced readability

## Word-Level Synchronization

The app supports karaoke-style subtitles where:
- Current word is **highlighted in yellow** and **bold**
- Previous words appear in **gray** (faded)
- Next 3 words are shown in **dim gray** as preview
- Each word appears/disappears exactly when spoken

## Troubleshooting

### Issue: "ImageMagick not found"
- Install ImageMagick from https://imagemagick.org/download/binaries/
- Update the path in `burn.py` line 2

### Issue: "ffmpeg not found"
- Install FFmpeg and add to system PATH
- Or: `pip install ffmpeg-python`

### Issue: "CUDA out of memory"
- Use a smaller Whisper model (tiny/base instead of medium/large)
- Reduce video resolution before processing

### Issue: Video takes very long to process
- Use a smaller Whisper model
- Break large videos into chunks
- Use GPU if available (install CUDA-enabled PyTorch)

### Issue: Subtitles not appearing in output video
- Verify SRT file format is correct (use tab to generate)
- Check video codec compatibility (MP4/H.264 recommended)
- Try burning again with different font settings

## Performance Tips

1. **For Quick Testing:** Use "tiny" model
2. **For Production:** Use "base" or "small" model
3. **GPU Acceleration:** Install CUDA-enabled PyTorch for 5-10x speedup
4. **Large Files:** Split videos into segments, process separately

## Advanced Usage

### Command-line Processing (without web UI)

```python
from generate_srt import transcribe, convert_to_srt, extract_word_timing
from burn import burn_subtitles_into_video, burn_word_level_subtitles

# Transcribe
result = transcribe("Audio/sample.wav", model_name="base")

# Generate SRT
srt_content = convert_to_srt(result, word_level=False)
with open("captions.srt", "w") as f:
    f.write(srt_content)

# Burn subtitles
burn_subtitles_into_video("Video/input.mp4", "captions.srt", "Video/output.mp4")
```

## Supported Video Formats

- MP4 (H.264/H.265)
- AVI
- MOV
- MKV (Matroska)
- FLV
- WMV

## Output Formats

- **Video:** MP4 (H.264 + AAC)
- **Subtitles:** SRT format with timestamps
- **Timing Data:** JSON with word-level timing

## License

This project uses:
- OpenAI Whisper (MIT License)
- MoviePy (MIT License)
- Streamlit (Streamlit License)

## Contributing

Feel free to enhance this project with:
- Better word-level timing extraction
- Additional subtitle styling options
- Batch processing capabilities
- Language translation support
- Cloud storage integration

## Future Enhancements

- 🌍 Multi-language support with automatic translation
- ✏️ Subtitle editor UI for manual correction
- 📊 Batch processing for multiple videos
- 🎨 Advanced styling (animations, fonts, positions)
- ☁️ Cloud storage integration (Google Drive, OneDrive)
- 🎞️ Video preview/trimming before processing
- 🔊 Audio enhancement and noise reduction
- 📱 Mobile-friendly interface

## Support

For issues or feature requests, please provide:
1. Error message and traceback
2. Video format and duration
3. Whisper model used
4. System specifications

---

Made with ❤️ for content creators
