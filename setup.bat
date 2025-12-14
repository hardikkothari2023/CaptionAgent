@echo off
REM Video Caption Generator - Setup Script for Windows

echo.
echo ================================================
echo   Video Caption Generator - Setup
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org
    pause
    exit /b 1
)

echo [OK] Python found:
python --version

echo.
echo ================================================
echo  Step 1: Creating virtual environment...
echo ================================================
if exist venv (
    echo Virtual environment already exists. Skipping...
) else (
    python -m venv venv
    echo [OK] Virtual environment created
)

echo.
echo ================================================
echo  Step 2: Activating virtual environment...
echo ================================================
call venv\Scripts\activate.bat
echo [OK] Virtual environment activated

echo.
echo ================================================
echo  Step 3: Installing dependencies...
echo ================================================
pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo [OK] Dependencies installed

echo.
echo ================================================
echo  Step 4: Checking ImageMagick...
echo ================================================
where magick >nul 2>&1
if errorlevel 1 (
    echo WARNING: ImageMagick not found in PATH
    echo Download from: https://imagemagick.org/download/binaries/
    echo After installation, update the path in burn.py
) else (
    echo [OK] ImageMagick found
    magick --version
)

echo.
echo ================================================
echo  Step 5: Checking FFmpeg...
echo ================================================
where ffmpeg >nul 2>&1
if errorlevel 1 (
    echo WARNING: FFmpeg not found in PATH
    echo Installing via pip...
    pip install ffmpeg-python
) else (
    echo [OK] FFmpeg found
    ffmpeg -version | find "ffmpeg version"
)

echo.
echo ================================================
echo  Setup Complete!
echo ================================================
echo.
echo To start the application, run:
echo   streamlit run app.py
echo.
echo The app will open at http://localhost:8501
echo.
pause
