# 🎬 Video Caption Generator - Quick Start Guide

## 🚀 Quick Start (5 Minutes)

### Windows Users:

1. **Double-click `setup.bat`** (one-time setup)
   - Creates virtual environment
   - Installs all dependencies
   - Checks for ImageMagick and FFmpeg

2. **Double-click `run.bat`** to start the app
   - Opens Streamlit interface at `http://localhost:8501`

### Mac/Linux Users:

```bash
# Setup (one-time)
chmod +x setup.sh
./setup.sh

# Run
chmod +x run.sh
./run.sh
```

---

## 📖 How to Use

### Step 1: Upload Video
- Click on "📤 Upload & Process" tab
- Select a video file (MP4, AVI, MOV, MKV, etc.)
- Click "Start Processing"

### Step 2: Configure Settings (Optional)
- Choose Whisper model:
  - **tiny** - Fastest, good for testing
  - **base** - Recommended balance (default)
  - **small** - Better accuracy
  - **medium** - Very accurate
  - **large** - Best accuracy, slowest
- Adjust subtitle styling:
  - Font size (16-48px)
  - Text color
  - Background color

### Step 3: Processing (Automatic)
The app will automatically:
1. Extract audio from video
2. Transcribe with AI (Whisper)
3. Generate subtitles with timing
4. Extract word-level data
5. Burn captions into video

### Step 4: Download Results
- **📝 Transcript Tab** → Download full text transcript
- **📌 Subtitles Tab** → Download SRT or word timing JSON
- **📥 Downloads Tab** → Download final video with captions

---

## 📊 What Each Tab Does

### 📤 Upload & Process
- Upload your video file
- Select Whisper model and subtitle styling
- Monitor processing progress (4 steps)
- See final status

### 📝 Transcript
- View complete AI-generated transcript
- Download as .txt file
- See word count and character count
- Copy text for use elsewhere

### 📌 Subtitles
- Preview SRT subtitle file format
- View word-level timing statistics
- See first 20 words with exact timing
- Download SRT or JSON timing file

### 📥 Downloads
- Download final MP4 video with burned captions
- Download subtitle file (SRT format)
- Download word timing data (JSON format)
- All files are ready to use immediately

---

## 🎨 Subtitle Features

### Karaoke-Style Word Synchronization
- **Current word** → Highlighted in YELLOW and BOLD
- **Previous words** → Shown in GRAY (faded)
- **Next words** → Shown as preview in DIM GRAY
- **Effect** → Words smoothly transition as speaker speaks

### Styling Options
- **Font sizes:** 16px (small) to 48px (large)
- **Colors:** Choose any color for text and background
- **Background:** Black, white, transparent, or semi-transparent
- **Position:** Always centered at bottom of video

---

## ⚙️ Model Comparison

| Need | Model | Speed | Accuracy |
|------|-------|-------|----------|
| Testing | tiny | 1 min | Fair |
| Quick job | base | 2-3 min | Good |
| Better results | small | 5-10 min | Excellent |
| Premium quality | medium | 15-30 min | Premium |
| Best accuracy | large | 30-60 min | Maximum |

**Time estimates based on 10-minute video**

---

## 💾 Output Files Explained

### 1. MP4 Video (with captions burned)
- File format: Video (H.264 codec)
- Size: Depends on original video (usually 20-200MB)
- Ready to: Upload to YouTube, share, archive
- Note: Captions are permanent (not separate tracks)

### 2. SRT Subtitle File
- File format: Text with timing
- Size: Small (usually <1MB)
- Format: Standard .srt format
- Ready to: Use with any video player as separate track
- Example:
```
1
00:00:01,000 --> 00:00:03,000
Hello world

2
00:00:03,500 --> 00:00:05,000
This is a test
```

### 3. JSON Word Timing
- File format: Text data (JSON)
- Size: Small (usually <100KB)
- Contains: Every word with exact start/end timing
- Ready to: Use for advanced subtitle editing or analysis

---

## 🔧 Troubleshooting

### Problem: "Python not found"
**Solution:** Install Python from python.org and add to PATH

### Problem: "ImageMagick not found"
**Solution:** 
- Download: https://imagemagick.org/download/binaries/
- Install and restart computer
- Update path in `burn.py` if needed

### Problem: "FFmpeg not found"
**Solution:** Run `pip install ffmpeg-python` or install FFmpeg manually

### Problem: Processing is very slow
**Solution:** 
- Use smaller Whisper model (tiny or base)
- Close other programs
- Check if GPU is available (would speed up significantly)

### Problem: Output video has no subtitles
**Solution:**
- Try different subtitle styling
- Verify SRT file is correct (check Subtitles tab)
- Try burning again

### Problem: Out of memory error
**Solution:**
- Use smaller Whisper model
- Reduce video resolution before uploading
- Close other programs
- Consider using GPU if available

---

## 🎯 Best Practices

### For YouTube Videos
- Use **base** or **small** model for good balance
- Font size: **28-32px** (easily readable)
- Color: **White on black** (standard YouTube style)

### For Social Media (TikTok, Instagram)
- Use **base** model (faster)
- Font size: **24-28px** (fits smaller screens)
- Color: **Bright colors** (white, yellow)

### For Professional Use
- Use **medium** or **large** model (best accuracy)
- Font size: **28px** (professional standard)
- Color: **Black with white** or **semi-transparent white**

### For Testing/Quick Work
- Use **tiny** model (fastest)
- Font size: **any** (doesn't matter for testing)
- Color: **any** (doesn't matter for testing)

---

## 📝 Example Workflow

```
1. Prepare Video
   └─ Record or find your video file
   └─ Ensure audio is clear
   └─ Optional: Edit video in separate tool

2. Open Video Caption Generator
   └─ Run app.py or double-click run.bat
   └─ Browser opens at localhost:8501

3. Configure Settings
   └─ Choose Whisper model (base recommended)
   └─ Set font size (28px is standard)
   └─ Pick colors (white text on black is safe)

4. Upload & Process
   └─ Select video file
   └─ Click "Start Processing"
   └─ Wait for completion (shows progress)

5. Review Results
   └─ Check Transcript tab (review for errors)
   └─ Check Subtitles tab (preview timing)
   └─ Make note of any corrections needed

6. Download & Use
   └─ Download MP4 with burned captions
   └─ Upload to YouTube/social media
   └─ Or download SRT for separate subtitle track
```

---

## 🎓 Understanding Whisper Models

**Whisper** is OpenAI's speech recognition AI. Different sizes:

- **tiny** (39MB) - Fast, suitable for testing
- **base** (140MB) - Good balance of speed and accuracy (RECOMMENDED)
- **small** (244MB) - Better accuracy, moderate speed
- **medium** (769MB) - High accuracy, slower
- **large** (1550MB) - Best accuracy, requires 10GB RAM+

First time you use a model, it downloads automatically (~100-1500MB).

---

## 🌟 Pro Tips

1. **First Time?** Start with **base** model
2. **Accuracy Matters?** Use **small** or **medium**
3. **Quick Test?** Use **tiny** model
4. **Storage Limited?** Process with tiny, then redo with base
5. **Multiple Videos?** Process overnight with large model
6. **Need Edits?** Download SRT file and edit in text editor
7. **Timing Off?** Try different Whisper model (sometimes varies)
8. **Video Too Long?** Split into segments and process separately

---

## 📞 Need Help?

### Common Issues & Fixes

| Issue | Try This |
|-------|----------|
| Slow processing | Use smaller model |
| Out of memory | Close other apps |
| Bad transcription | Try different Whisper model |
| No subtitles visible | Check SRT file, try different colors |
| Audio not detected | Ensure video has audio track |

---

## 🎬 What's Next?

### You Can Also:
- ✏️ Edit SRT file to fix any transcription errors
- 🎨 Use online SRT editors to customize styling
- 📤 Upload directly to YouTube with burned captions
- 🌍 Translate SRT file for multiple languages
- 🎞️ Create clips from the captioned video
- 📊 Analyze transcript for keywords

---

Made with ❤️ by the Video Caption Generator team
