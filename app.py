import streamlit as st
import os
import tempfile
import shutil
import json
from pathlib import Path
from datetime import datetime

# Import custom modules
from extract_audio import extract_audio_from_video
from generate_srt import transcribe, convert_to_srt, extract_word_timing, save_word_timing_json
from burn import burn_subtitles_into_video, burn_word_level_subtitles


# Configure Streamlit page
st.set_page_config(
    page_title="🎬 Video Caption Generator",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
<style>
    .main {
        padding-top: 1rem;
    }
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 1.1rem;
        font-weight: 600;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 5px;
        padding: 15px;
        margin: 10px 0;
    }
    .info-box {
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        border-radius: 5px;
        padding: 15px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)


def initialize_session_state():
    """Initialize session state variables."""
    if 'processed' not in st.session_state:
        st.session_state.processed = False
    if 'transcript_text' not in st.session_state:
        st.session_state.transcript_text = None
    if 'words_data' not in st.session_state:
        st.session_state.words_data = None
    if 'output_video_path' not in st.session_state:
        st.session_state.output_video_path = None
    if 'srt_content' not in st.session_state:
        st.session_state.srt_content = None
    if 'upload_time' not in st.session_state:
        st.session_state.upload_time = None


def create_temp_directories():
    """Create temporary directories for processing."""
    os.makedirs("Video", exist_ok=True)
    os.makedirs("Audio", exist_ok=True)
    os.makedirs("captions", exist_ok=True)


def get_unique_filename(base_name, extension):
    """Generate unique filename with timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    name_without_ext = os.path.splitext(base_name)[0]
    return f"{name_without_ext}_{timestamp}{extension}"


def process_video(video_path, model_name="base", generate_word_level=True):
    """Process video through the entire pipeline."""
    try:
        progress_container = st.container()
        
        with progress_container:
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Step 1: Extract Audio
            status_text.text("📍 Step 1/4: Extracting audio from video...")
            progress_bar.progress(20)
            
            audio_filename = get_unique_filename("extracted_audio", ".wav")
            audio_path = f"Audio/{audio_filename}"
            extract_audio_from_video(video_path, audio_path)
            st.session_state.upload_time = datetime.now()
            
            # Step 2: Transcribe Audio
            status_text.text("📍 Step 2/4: Transcribing audio with Whisper...")
            progress_bar.progress(40)
            
            transcript_result = transcribe(audio_path, model_name=model_name)
            st.session_state.transcript_text = transcript_result['text']
            
            # Step 3: Generate SRT Files
            status_text.text("📍 Step 3/4: Generating subtitle files...")
            progress_bar.progress(60)
            
            # Segment-level SRT
            srt_content = convert_to_srt(transcript_result, word_level=False)
            st.session_state.srt_content = srt_content
            
            srt_filename = get_unique_filename("captions", ".srt")
            srt_path = f"captions/{srt_filename}"
            with open(srt_path, "w", encoding="utf-8") as f:
                f.write(srt_content)
            
            # Word-level data
            if generate_word_level:
                words_data = extract_word_timing(transcript_result)
                st.session_state.words_data = words_data
                
                json_filename = get_unique_filename("word_timing", ".json")
                json_path = f"captions/{json_filename}"
                save_word_timing_json(words_data, json_path)
            
            # Step 4: Burn Subtitles
            status_text.text("📍 Step 4/4: Burning subtitles into video...")
            progress_bar.progress(80)
            
            # Burn segment-level subtitles
            output_filename = get_unique_filename("output_burned", ".mp4")
            output_path = f"Video/{output_filename}"
            burn_subtitles_into_video(video_path, srt_path, output_path)
            st.session_state.output_video_path = output_path
            
            progress_bar.progress(100)
            status_text.text("✅ Processing complete!")
            
            return True, {
                'audio_path': audio_path,
                'srt_path': srt_path,
                'json_path': json_path if generate_word_level else None,
                'output_video_path': output_path
            }
    
    except Exception as e:
        st.error(f"❌ Error during processing: {str(e)}")
        return False, None


def display_transcript_tab():
    """Display transcript tab."""
    st.subheader("📝 Full Transcript")
    
    if st.session_state.transcript_text:
        st.text_area(
            "Generated Transcript",
            value=st.session_state.transcript_text,
            height=300,
            disabled=True,
            label_visibility="collapsed"
        )
        
        # Copy and download buttons
        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                label="📥 Download Transcript (.txt)",
                data=st.session_state.transcript_text,
                file_name=f"transcript_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain"
            )
        with col2:
            # Character and word count
            char_count = len(st.session_state.transcript_text)
            word_count = len(st.session_state.transcript_text.split())
            st.metric("Stats", f"{word_count} words, {char_count} characters")
    else:
        st.info("No transcript available. Process a video first.")


def display_subtitles_tab():
    """Display subtitles preview tab."""
    st.subheader("📌 Subtitles Preview")
    
    if st.session_state.srt_content:
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.text_area(
                "SRT Format",
                value=st.session_state.srt_content,
                height=400,
                disabled=True,
                label_visibility="collapsed"
            )
        
        with col2:
            st.download_button(
                label="📥 Download SRT",
                data=st.session_state.srt_content,
                file_name=f"captions_{datetime.now().strftime('%Y%m%d_%H%M%S')}.srt",
                mime="text/plain"
            )
        
        # Word timing stats
        if st.session_state.words_data:
            st.divider()
            st.markdown("### 📊 Word-Level Timing Data")
            
            num_words = len(st.session_state.words_data)
            total_duration = st.session_state.words_data[-1]['end'] if st.session_state.words_data else 0
            avg_word_duration = total_duration / num_words if num_words > 0 else 0
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Words", num_words)
            col2.metric("Duration", f"{total_duration:.2f}s")
            col3.metric("Avg Word Duration", f"{avg_word_duration:.3f}s")
            
            # Show first 20 words with timing
            st.markdown("#### First 20 Words Timeline")
            for i, word_info in enumerate(st.session_state.words_data[:20]):
                duration = word_info['end'] - word_info['start']
                st.write(f"**{i+1}.** {word_info['word']} `[{word_info['start']:.2f}s - {word_info['end']:.2f}s]` ({duration:.3f}s)")
    else:
        st.info("No subtitles available. Process a video first.")


def display_downloads_tab():
    """Display downloads tab."""
    st.subheader("📥 Download Generated Files")
    
    if st.session_state.output_video_path and os.path.exists(st.session_state.output_video_path):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🎬 Burned Video")
            file_size = os.path.getsize(st.session_state.output_video_path) / (1024 * 1024)
            st.info(f"File size: {file_size:.2f} MB")
            
            with open(st.session_state.output_video_path, "rb") as video_file:
                st.download_button(
                    label="⬇️ Download Video with Captions (MP4)",
                    data=video_file,
                    file_name=f"video_with_captions_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4",
                    mime="video/mp4",
                    use_container_width=True
                )
        
        with col2:
            st.markdown("#### 📄 Subtitle Files")
            if st.session_state.srt_content:
                st.download_button(
                    label="⬇️ Download SRT File",
                    data=st.session_state.srt_content,
                    file_name=f"captions_{datetime.now().strftime('%Y%m%d_%H%M%S')}.srt",
                    mime="text/plain",
                    use_container_width=True
                )
            
            if st.session_state.words_data:
                words_json = json.dumps(st.session_state.words_data, indent=2, ensure_ascii=False)
                st.download_button(
                    label="⬇️ Download Word Timing (JSON)",
                    data=words_json,
                    file_name=f"word_timing_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                    mime="application/json",
                    use_container_width=True
                )
    else:
        st.info("No output video available. Process a video first.")


def main():
    """Main Streamlit application."""
    initialize_session_state()
    create_temp_directories()
    
    # Header
    st.title("🎬 Video Caption Generator")
    st.markdown("Convert your videos to auto-captioned masterpieces with AI-powered transcription")
    
    # Sidebar Configuration
    with st.sidebar:
        st.header("⚙️ Settings")
        
        model_choice = st.selectbox(
            "🤖 Whisper Model",
            ["tiny", "base", "small", "medium", "large"],
            index=1,
            help="tiny=fastest, large=most accurate. Larger models take more time but are more accurate."
        )
        
        st.divider()
        
        st.subheader("🎨 Subtitle Styling")
        
        col1, col2 = st.columns(2)
        with col1:
            font_size = st.slider("Font Size", 16, 48, 28)
        with col2:
            text_color = st.color_picker("Text Color", "#FFFFFF")
        
        bg_color = st.selectbox(
            "Background Color",
            ["black", "white", "transparent", "semi-transparent"],
            help="Choose background style for subtitles"
        )
        
        st.divider()
        
        st.info("""
        💡 **Tips:**
        - Start with 'base' model for good balance
        - Use 'tiny' for quick testing
        - Use 'small'/'medium' for production
        - Processing time depends on video length
        """)
    
    # Main Content
    tab1, tab2, tab3, tab4 = st.tabs(["📤 Upload & Process", "📝 Transcript", "📌 Subtitles", "📥 Downloads"])
    
    with tab1:
        st.subheader("📤 Upload Video")
        
        uploaded_file = st.file_uploader(
            "Choose a video file",
            type=["mp4", "avi", "mov", "mkv", "flv", "wmv"],
            help="Supported formats: MP4, AVI, MOV, MKV, FLV, WMV"
        )
        
        if uploaded_file:
            # Save uploaded file
            temp_video_path = f"Video/temp_{uploaded_file.name}"
            with open(temp_video_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            st.success(f"✅ Video uploaded: {uploaded_file.name}")
            
            # Show video info
            col1, col2, col3 = st.columns(3)
            col1.metric("File Size", f"{uploaded_file.size / (1024*1024):.2f} MB")
            col2.metric("File Type", uploaded_file.type)
            col3.metric("Whisper Model", model_choice.upper())
            
            st.divider()
            
            # Process button
            if st.button("🚀 Start Processing", use_container_width=True, type="primary"):
                success, result = process_video(
                    temp_video_path,
                    model_name=model_choice,
                    generate_word_level=True
                )
                
                if success:
                    st.session_state.processed = True
                    st.balloons()
                    
                    success_message = """
                    ✅ **Processing Complete!**
                    
                    Your video has been successfully processed with:
                    - ✅ Audio extraction
                    - ✅ Whisper transcription
                    - ✅ SRT subtitle generation
                    - ✅ Word-level timing
                    - ✅ Subtitle burning
                    
                    Check the other tabs to view your transcript, subtitles, and download files!
                    """
                    st.markdown(success_message)
            
            # Show status if already processed
            if st.session_state.processed and st.session_state.transcript_text:
                st.info("✅ This video has been processed. View details in other tabs.")
        else:
            st.info("👆 Upload a video file to get started")
    
    with tab2:
        display_transcript_tab()
    
    with tab3:
        display_subtitles_tab()
    
    with tab4:
        display_downloads_tab()
    
    # Footer
    st.divider()
    st.markdown("""
    <div style='text-align: center; color: gray; font-size: 0.9em;'>
        <p>🎬 Video Caption Generator | Powered by OpenAI Whisper & Streamlit</p>
        <p>Built with ❤️ for content creators</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
