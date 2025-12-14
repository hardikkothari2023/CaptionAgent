# 📋 Installation & Setup Guide

## System Requirements

### Minimum Requirements
- **OS:** Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **Python:** 3.8 or higher
- **RAM:** 4GB minimum
- **Storage:** 10GB free space (for models + processing)
- **Internet:** Required for first-time model download

### Recommended Requirements
- **Python:** 3.9 or 3.10
- **RAM:** 8GB+
- **GPU:** NVIDIA GPU with CUDA support (5-10x faster)
- **Storage:** 20GB+ free space
- **Internet Speed:** Broadband (faster model downloads)

---

## 🪟 Windows Installation

### Step 1: Install Python

1. Download Python 3.10 from https://www.python.org/downloads/
2. **IMPORTANT:** Check "Add Python to PATH" during installation
3. Verify installation:
   ```cmd
   python --version
   ```
   Should show: `Python 3.10.x` or higher

### Step 2: Install ImageMagick

1. Download from: https://imagemagick.org/download/binaries/
   - File: `ImageMagick-7.1.2-Q16-HDRI-x64-dll.exe`
2. Run installer and note the installation path
3. Default path is usually: `C:\Program Files\ImageMagick-7.1.2-Q16-HDRI`

### Step 3: Install Dependencies

```cmd
# Navigate to project directory
cd "d:\Project 7 sem\Video_Caption_Generater"

# Run setup script (automatic)
setup.bat

# OR manual installation:
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Step 4: Verify Installation

```cmd
# Activate virtual environment
venv\Scripts\activate

# Check Python packages
pip list

# Launch app
streamlit run app.py
```

### Step 5: First Run

- App should open at `http://localhost:8501`
- First time using a Whisper model? It will download automatically (~100-1500MB)
- This is normal - wait for download to complete

---

## 🍎 macOS Installation

### Step 1: Install Python

```bash
# Using Homebrew (recommended)
brew install python@3.10

# Verify installation
python3 --version
```

### Step 2: Install System Tools

```bash
# Install ImageMagick
brew install imagemagick

# Install FFmpeg
brew install ffmpeg

# Verify installations
magick --version
ffmpeg -version
```

### Step 3: Install Python Dependencies

```bash
# Navigate to project directory
cd ~/Projects/Video_Caption_Generater

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 4: Run Application

```bash
# Activate virtual environment
source venv/bin/activate

# Launch Streamlit app
streamlit run app.py
```

---

## 🐧 Linux Installation

### Step 1: Install Python & Tools

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv

# Install ImageMagick and FFmpeg
sudo apt-get install imagemagick ffmpeg

# Verify installations
python3 --version
magick --version
ffmpeg -version
```

### Step 2: Create Virtual Environment

```bash
# Navigate to project directory
cd ~/Projects/Video_Caption_Generater

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install from requirements
pip install -r requirements.txt
```

### Step 4: Run Application

```bash
# Make sure venv is activated
source venv/bin/activate

# Launch app
streamlit run app.py
```

---

## 🤖 GPU Acceleration Setup (Optional)

### NVIDIA GPU with CUDA

```bash
# Install CUDA-enabled PyTorch (replaces CPU version)
pip uninstall torch
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Check GPU is Working

```python
python -c "import torch; print(torch.cuda.is_available())"
# Should print: True if GPU detected
```

### Performance Improvement
- CPU: ~1-2 min per 10-min video (tiny model)
- GPU: ~10-30 seconds per 10-min video (tiny model)
- 5-10x faster overall!

---

## ⚡ Quick Installation Summary

### Windows (Fastest)
```cmd
cd "d:\Project 7 sem\Video_Caption_Generater"
setup.bat
run.bat
```

### macOS / Linux
```bash
cd ~/Projects/Video_Caption_Generater
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔍 Troubleshooting Installation

### Issue: "Python not found"
```bash
# Windows
where python
# Should show Python path

# Mac/Linux  
which python3
# Should show Python path
```
**Solution:** Add Python to PATH or use full path

### Issue: "pip install" fails
```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing again
pip install -r requirements.txt
```

### Issue: "ImageMagick not found"
- Windows: Reinstall ImageMagick and add to PATH
- Mac: `brew install imagemagick`
- Linux: `apt-get install imagemagick`

### Issue: "FFmpeg not found"
- Windows: `pip install ffmpeg-python`
- Mac: `brew install ffmpeg`
- Linux: `apt-get install ffmpeg`

### Issue: Permission Denied (Mac/Linux)
```bash
# Fix permission issues
chmod +x setup.sh run.sh launch.py
```

### Issue: Virtual Environment Won't Activate

```bash
# Recreate virtual environment
rm -rf venv
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

---

## 📦 Dependency Information

### Core Dependencies
- **streamlit** (1.28+) - Web framework
- **moviepy** (1.0+) - Video/audio processing
- **openai-whisper** (20230314+) - Speech recognition
- **pysrt** (1.1+) - Subtitle format
- **torch** (2.0+) - ML framework
- **pillow** (9.5+) - Image processing

### System Dependencies
- **ImageMagick** (7.0+) - Text rendering for subtitles
- **FFmpeg** (4.0+) - Media codec support
- **libsndfile** - Audio file support

---

## 🚀 First Time Running

### What Happens First Run

1. **Streamlit loads** - Creates cache directory
2. **You upload video** - Video is saved to `/Video` folder
3. **Processing starts:**
   - Audio extraction (~30 seconds)
   - Whisper downloads model (~1-5 minutes first time)
   - Transcription starts (~1-3 minutes for 10-min video)
   - SRT generation (few seconds)
   - Video burning (~2-5 minutes)
4. **Results available** - Check all tabs for outputs

### Expected Times
- **First run:** 10-20 minutes (includes model download)
- **Subsequent runs:** 5-10 minutes (model cached)
- **With GPU:** 2-5 minutes

### Downloaded Files
- **Model files:** `~/.cache/huggingface/hub/` (1-2GB depending on model)
- **Streamlit cache:** `~/.streamlit/`

---

## ✅ Verify Installation

### Test Script

```python
# Create test.py
import streamlit as st
import torch
import whisper
import moviepy
import pysrt

st.title("Installation Check")

try:
    st.success("✅ Streamlit working")
    st.write(f"PyTorch version: {torch.__version__}")
    st.write(f"GPU available: {torch.cuda.is_available()}")
    
    # Test Whisper
    model = whisper.load_model("tiny")
    st.write("✅ Whisper model loaded")
    
    st.write("✅ All dependencies working!")
except Exception as e:
    st.error(f"❌ Error: {e}")
```

Run with: `streamlit run test.py`

---

## 🔧 Advanced Configuration

### Modify Model Download Location

```bash
# Linux/Mac
export HF_HOME=/custom/path

# Windows
set HF_HOME=C:\custom\path
```

### Use Specific Python Version

```bash
# Create venv with Python 3.10
python3.10 -m venv venv
```

### Install CPU-Only PyTorch

```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

---

## 🎯 Next Steps After Installation

1. ✅ Read [QUICK_START.md](QUICK_START.md)
2. ✅ Run test with sample video
3. ✅ Explore settings in sidebar
4. ✅ Try different Whisper models
5. ✅ Experiment with subtitle styling

---

## 📞 Still Having Issues?

### Debug Information Needed
- Python version: `python --version`
- OS and version: `uname -a`
- Installation path: `where python`
- Error message: Full text
- Steps taken: What you did before error

### Try This First
1. Update pip: `pip install --upgrade pip`
2. Reinstall requirements: `pip install -r requirements.txt --upgrade`
3. Restart terminal/IDE
4. Restart computer
5. Check internet connection (model downloads)

---

## 🎉 Ready to Start!

Once installation is complete and verified:

```bash
# Activate environment and run app
# Windows:
venv\Scripts\activate && streamlit run app.py

# Mac/Linux:
source venv/bin/activate && streamlit run app.py
```

The app opens at: **http://localhost:8501**

**Happy captioning!** 🎬✨
