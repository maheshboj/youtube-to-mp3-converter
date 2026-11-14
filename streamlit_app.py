import os
import glob
import subprocess
import streamlit as st

st.set_page_config(
    page_title="YouTube to MP3 Converter",
    page_icon="🎵",
    layout="centered"
)

# Application Title & Description
st.title("🎵 YouTube to MP3 Converter")
st.markdown("Convert and extract high-quality MP3 audio from any YouTube link.")

# Default parameters
default_link = "https://youtu.be/eShagnIgvZA?si=bJKHR-u97jbgojrd"
default_output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "downloads"))
os.makedirs(default_output_dir, exist_ok=True)

# Form controls
with st.container():
    url_input = st.text_input(
        "YouTube Video URL:",
        value=default_link,
        placeholder="https://www.youtube.com/watch?v=..."
    )

    output_dir_input = st.text_input(
        "Destination Folder:",
        value=default_output_dir,
        help="The local folder where converted MP3 files will be stored."
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        convert_clicked = st.button("🚀 Convert to MP3", type="primary", use_container_width=True)
    with col2:
        if st.button("📂 Open Output Folder", use_container_width=True):
            if os.path.exists(output_dir_input):
                os.startfile(output_dir_input)
                st.toast("Opened destination folder in File Explorer!", icon="📂")
            else:
                st.error("Folder does not exist.")

if convert_clicked:
    if not url_input.strip():
        st.warning("Please provide a valid YouTube URL.")
    else:
        os.makedirs(output_dir_input, exist_ok=True)
        with st.spinner("Downloading audio and converting to MP3... Please wait..."):
            cmd = [
                "yt-dlp",
                "-x",
                "--audio-format", "mp3",
                "--audio-quality", "0",
                "--output", os.path.join(output_dir_input, "%(title)s.%(ext)s"),
                url_input.strip()
            ]
            try:
                result = subprocess.run(cmd, capture_output=True, text=True, check=True)
                st.success("🎉 Conversion successful!")
            except subprocess.CalledProcessError as e:
                err_msg = e.stderr or e.stdout or str(e)
                st.error("❌ Failed to download or convert the video.")
                st.code(err_msg, language="bash")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# Destination folder inspection section
st.divider()
st.subheader("📁 Converted Files in Output Folder")
st.caption(f"Location: `{output_dir_input}`")

if os.path.exists(output_dir_input):
    mp3_files = glob.glob(os.path.join(output_dir_input, "*.mp3"))
    if mp3_files:
        # Sort latest first
        mp3_files.sort(key=os.path.getmtime, reverse=True)
        for idx, file_path in enumerate(mp3_files):
            filename = os.path.basename(file_path)
            file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
            mod_time = os.path.getmtime(file_path)
            
            with st.expander(f"🎶 {filename} ({file_size_mb:.2f} MB)", expanded=(idx == 0)):
                st.write(f"**Full Path:** `{file_path}`")
                
                # Audio player widget
                with open(file_path, "rb") as audio_file:
                    audio_bytes = audio_file.read()
                    st.audio(audio_bytes, format="audio/mp3")
                    
                    st.download_button(
                        label="⬇️ Download MP3 to your browser",
                        data=audio_bytes,
                        file_name=filename,
                        mime="audio/mp3",
                        key=f"dl_{idx}"
                    )
    else:
        st.info("No MP3 files found in this folder yet. Click 'Convert to MP3' to convert.")
else:
    st.info("The specified output folder does not exist yet.")
