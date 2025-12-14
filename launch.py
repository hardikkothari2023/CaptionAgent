#!/usr/bin/env python
"""
Video Caption Generator - Launcher Script
This script helps launch the Streamlit app with proper error handling.
"""

import os
import sys
import subprocess
import platform
from pathlib import Path


def check_python_version():
    """Check if Python version is 3.8 or higher."""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        print(f"   Current version: {sys.version}")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    return True


def check_dependencies():
    """Check if required packages are installed."""
    required_packages = {
        'streamlit': 'Streamlit Web Framework',
        'moviepy': 'Video Processing',
        'whisper': 'Audio Transcription',
        'pysrt': 'Subtitle Format',
    }
    
    print("\n📦 Checking dependencies...")
    missing = []
    
    for package, description in required_packages.items():
        try:
            __import__(package)
            print(f"  ✅ {description} ({package})")
        except ImportError:
            print(f"  ❌ {description} ({package})")
            missing.append(package)
    
    if missing:
        print(f"\n⚠️  Missing packages: {', '.join(missing)}")
        print(f"\nTo install missing packages, run:")
        print(f"  pip install {' '.join(missing)}")
        return False
    
    return True


def check_imagemagick():
    """Check if ImageMagick is installed."""
    print("\n🎨 Checking ImageMagick...")
    
    if platform.system() == "Windows":
        paths_to_check = [
            r"C:\Program Files\ImageMagick-7.1.2-Q16-HDRI\magick.exe",
            r"C:\Program Files\ImageMagick\magick.exe",
            r"C:\Program Files (x86)\ImageMagick\magick.exe",
        ]
        
        found = False
        for path in paths_to_check:
            if os.path.exists(path):
                print(f"  ✅ ImageMagick found at {path}")
                found = True
                break
        
        if not found:
            print("  ⚠️  ImageMagick not found in standard locations")
            print("     Download from: https://imagemagick.org/download/binaries/")
            print("     After installation, restart this script")
            return False
    else:
        # On Mac/Linux, check using which command
        result = subprocess.run(['which', 'magick'], capture_output=True)
        if result.returncode == 0:
            print(f"  ✅ ImageMagick found")
        else:
            print("  ⚠️  ImageMagick not found")
            print("     Install with: brew install imagemagick (Mac) or apt-get install imagemagick (Linux)")
            return False
    
    return True


def check_ffmpeg():
    """Check if FFmpeg is installed."""
    print("\n🎬 Checking FFmpeg...")
    
    result = subprocess.run(['ffmpeg', '-version'], capture_output=True, text=True)
    
    if result.returncode == 0:
        version_line = result.stdout.split('\n')[0]
        print(f"  ✅ FFmpeg found")
        print(f"     {version_line}")
        return True
    else:
        print("  ⚠️  FFmpeg not found")
        if platform.system() == "Windows":
            print("     Try: pip install ffmpeg-python")
        else:
            print("     Install with: brew install ffmpeg (Mac) or apt-get install ffmpeg (Linux)")
        return False


def create_required_directories():
    """Create required directories."""
    print("\n📁 Creating directories...")
    
    dirs = ['Video', 'Audio', 'captions']
    for dir_name in dirs:
        os.makedirs(dir_name, exist_ok=True)
        print(f"  ✅ {dir_name}/")


def launch_streamlit():
    """Launch the Streamlit app."""
    print("\n" + "="*60)
    print("🚀 Starting Video Caption Generator...")
    print("="*60)
    print("\n📍 The app will open at: http://localhost:8501")
    print("📍 Press Ctrl+C to stop the server\n")
    
    # Check if app.py exists
    if not os.path.exists('app.py'):
        print("❌ app.py not found in current directory")
        print(f"   Current directory: {os.getcwd()}")
        return False
    
    try:
        subprocess.run(['streamlit', 'run', 'app.py'])
    except KeyboardInterrupt:
        print("\n\n✅ Server stopped. Thanks for using Video Caption Generator!")
    except Exception as e:
        print(f"\n❌ Error launching Streamlit: {e}")
        return False
    
    return True


def main():
    """Main entry point."""
    print("\n" + "="*60)
    print("🎬 Video Caption Generator - Launcher")
    print("="*60)
    
    # Check Python version
    if not check_python_version():
        return 1
    
    # Check dependencies
    if not check_dependencies():
        print("\n⚠️  Some dependencies are missing!")
        print("   Run: pip install -r requirements.txt")
        return 1
    
    # Check system tools
    imagemagick_ok = check_imagemagick()
    ffmpeg_ok = check_ffmpeg()
    
    if not (imagemagick_ok and ffmpeg_ok):
        print("\n⚠️  Some system tools are missing. Install them and try again.")
        input("\nPress Enter to continue anyway (may experience errors)...")
    
    # Create directories
    create_required_directories()
    
    # Launch app
    if launch_streamlit():
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())
