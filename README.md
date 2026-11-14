# 🎵 YouTube to MP3 Converter Application

A versatile desktop and web application to extract and convert YouTube videos or songs into high-quality MP3 files using `yt-dlp` and `ffmpeg`.

---

## 🌟 Features

- **Streamlit Web UI**:
  - Clean web interface to input any YouTube URL.
  - Custom destination folder selection.
  - "Open Output Folder" button to open the folder directly in Windows Explorer.
  - In-browser MP3 audio player with file size & modification details.
  - In-browser direct MP3 download button.
- **Tkinter Desktop GUI**:
  - Standalone desktop graphical application.
  - Folder browser dialogue and conversion status bar.
- **CLI Support**:
  - Run conversions directly from terminal / scripts.

---

## 🛠️ Prerequisites

1. **Python 3.10+**: Ensure Python is installed and added to `PATH`.
2. **FFmpeg**: Required by `yt-dlp` to extract and encode audio into MP3.
   - On Windows, install via winget or chocolatey:
     ```powershell
     winget install Gyan.FFmpeg
     ```
     Or ensure `ffmpeg.exe` is in your system `PATH`.

---

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/<YOUR_USERNAME>/<REPO_NAME>.git
   cd <REPO_NAME>
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Execution Guide

### Option 1: Streamlit Web Application (Recommended)

Run the Streamlit application using:
```bash
streamlit run streamlit_app.py
```
*Or on Windows, simply double-click **`run_streamlit.bat`**.*

The browser will open at `http://localhost:8501`. Enter your YouTube link and click **"Convert to MP3"**.

---

### Option 2: Desktop GUI (Tkinter)

Run the desktop interface:
```bash
python app.py
```
*Or on Windows, double-click **`run_app.bat`**.*

---

### Option 3: Command Line (CLI)

Convert a link directly to a specific folder:
```bash
python app.py "<YOUTUBE_URL>" "C:\path\to\save\directory"
```

Example:
```bash
python app.py "https://youtu.be/eShagnIgvZA?si=bJKHR-u97jbgojrd" "./downloads"
```

---

## 📁 Project Structure

```text
├── streamlit_app.py    # Streamlit web application
├── app.py              # Tkinter desktop GUI & CLI converter
├── run_streamlit.bat   # Windows one-click launcher for Streamlit
├── run_app.bat         # Windows one-click launcher for Tkinter GUI
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules for media files & cache
└── README.md           # Documentation
```
