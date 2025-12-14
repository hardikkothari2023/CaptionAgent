"""
Video Caption Generator - Configuration File
Customize settings here before running the app
"""

# =============================================================================
# WHISPER MODEL CONFIGURATION
# =============================================================================

# Default Whisper model to use
# Options: "tiny", "base", "small", "medium", "large"
DEFAULT_MODEL = "base"

# Models available in the UI
AVAILABLE_MODELS = ["tiny", "base", "small", "medium", "large"]

# Model descriptions for UI
MODEL_DESCRIPTIONS = {
    "tiny": "⚡⚡⚡⚡⚡ Fastest (39MB) - Good for testing and quick jobs",
    "base": "⚡⚡⚡⚡ Recommended (140MB) - Best balance of speed and accuracy",
    "small": "⚡⚡⚡ Better accuracy (244MB) - Good for production",
    "medium": "⚡⚡ High accuracy (769MB) - Very accurate, slower processing",
    "large": "⚡ Best accuracy (1550MB) - Maximum accuracy, requires 10GB+ RAM",
}


# =============================================================================
# SUBTITLE STYLING DEFAULTS
# =============================================================================

# Default font size (16-48)
DEFAULT_FONT_SIZE = 28

# Default text color (hex code)
DEFAULT_TEXT_COLOR = "#FFFFFF"  # White

# Default background color
# Options: "black", "white", "transparent", "semi-transparent"
DEFAULT_BG_COLOR = "black"

# Font to use (must be available on system)
# Options: "Arial", "Helvetica", "Times New Roman", "Courier New", etc.
SUBTITLE_FONT = "Arial"

# Subtitle position
# Options: ("center", "top"), ("center", "bottom"), ("left", "bottom"), etc.
SUBTITLE_POSITION = ("center", "bottom")


# =============================================================================
# KARAOKE/WORD-LEVEL SETTINGS
# =============================================================================

# Enable word-level subtitle generation
ENABLE_WORD_LEVEL = True

# Default highlight color for current word
WORD_HIGHLIGHT_COLOR = "#FFFF00"  # Yellow

# Number of next words to show as preview
SHOW_NEXT_WORDS = 3

# Color for previous words (faded)
PREVIOUS_WORDS_COLOR = "#808080"  # Gray

# Color for next words (preview)
NEXT_WORDS_COLOR = "#808080"  # Gray


# =============================================================================
# VIDEO PROCESSING
# =============================================================================

# Video codec (libx264 is most compatible)
VIDEO_CODEC = "libx264"

# Audio codec
AUDIO_CODEC = "aac"

# Video quality (1-51, lower is better)
# 18-28 is recommended for good quality vs file size
VIDEO_CRF = 23

# Thread count for encoding (0 = auto)
THREAD_COUNT = 0


# =============================================================================
# FILE PATHS
# =============================================================================

# Directories for input/output
VIDEO_DIR = "Video"
AUDIO_DIR = "Audio"
CAPTIONS_DIR = "captions"

# Temporary file cleanup
# Set to True to automatically delete temporary files after processing
AUTO_CLEANUP_TEMP = True

# Maximum file size for uploads (in MB)
MAX_UPLOAD_SIZE = 1000  # 1GB


# =============================================================================
# UI CONFIGURATION
# =============================================================================

# App title
APP_TITLE = "🎬 Video Caption Generator"

# App icon
APP_ICON = "🎬"

# Page layout ("wide" or "centered")
PAGE_LAYOUT = "wide"

# Sidebar state ("expanded" or "collapsed")
SIDEBAR_STATE = "expanded"

# Show performance metrics
SHOW_METRICS = True

# Auto-play after processing
AUTO_PLAY_PROCESSED_VIDEO = False


# =============================================================================
# LOGGING AND DEBUG
# =============================================================================

# Log level: "DEBUG", "INFO", "WARNING", "ERROR"
LOG_LEVEL = "INFO"

# Show detailed processing logs
SHOW_PROCESSING_LOGS = False

# Save processing logs to file
SAVE_LOGS = True

# Log file path
LOG_FILE = "logs/app.log"


# =============================================================================
# PERFORMANCE TUNING
# =============================================================================

# Use GPU if available (requires CUDA-enabled PyTorch)
USE_GPU = True

# Number of worker processes
NUM_WORKERS = 4

# Batch processing (experimental)
ENABLE_BATCH_PROCESSING = False


# =============================================================================
# ADVANCED FEATURES (Experimental)
# =============================================================================

# Enable speaker identification (experimental)
ENABLE_SPEAKER_ID = False

# Enable automatic language detection
ENABLE_AUTO_LANGUAGE = True

# Supported languages for transcription
SUPPORTED_LANGUAGES = [
    "en",  # English
    "es",  # Spanish
    "fr",  # French
    "de",  # German
    "it",  # Italian
    "pt",  # Portuguese
    "nl",  # Dutch
    "ru",  # Russian
    "zh",  # Chinese
    "ja",  # Japanese
]


# =============================================================================
# UI CUSTOMIZATION
# =============================================================================

# Custom CSS
CUSTOM_CSS = """
<style>
    .main {
        padding-top: 1rem;
    }
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 1.1rem;
        font-weight: 600;
    }
</style>
"""

# Color scheme
PRIMARY_COLOR = "#FF6B6B"
SECONDARY_COLOR = "#4ECDC4"


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def get_model_info(model_name):
    """Get information about a specific model."""
    return MODEL_DESCRIPTIONS.get(model_name, "Unknown model")


def get_all_config():
    """Get all configuration as a dictionary."""
    return {
        'default_model': DEFAULT_MODEL,
        'available_models': AVAILABLE_MODELS,
        'default_font_size': DEFAULT_FONT_SIZE,
        'default_text_color': DEFAULT_TEXT_COLOR,
        'default_bg_color': DEFAULT_BG_COLOR,
        'enable_word_level': ENABLE_WORD_LEVEL,
        'video_codec': VIDEO_CODEC,
        'audio_codec': AUDIO_CODEC,
    }


if __name__ == "__main__":
    # Print all configuration
    print("Video Caption Generator - Configuration")
    print("=" * 60)
    print(f"Default Model: {DEFAULT_MODEL}")
    print(f"Available Models: {', '.join(AVAILABLE_MODELS)}")
    print(f"Default Font Size: {DEFAULT_FONT_SIZE}px")
    print(f"Default Colors: Text={DEFAULT_TEXT_COLOR}, BG={DEFAULT_BG_COLOR}")
    print(f"Word-Level Subtitles: {'Enabled' if ENABLE_WORD_LEVEL else 'Disabled'}")
    print(f"Video Codec: {VIDEO_CODEC}")
    print(f"Audio Codec: {AUDIO_CODEC}")
    print("=" * 60)
