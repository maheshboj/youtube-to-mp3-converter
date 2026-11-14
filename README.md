# 🎵 YouTube to MP3 Converter Application

A versatile web and desktop application to extract and convert YouTube videos or songs into high-quality MP3 files using `yt-dlp` and `ffmpeg`.

Can be run **in Docker (containerized)** without needing Python/FFmpeg installed locally, or run natively via **Streamlit** / **Tkinter desktop GUI**.

---

## 🌟 Features

- **Docker Containerized**: Run anywhere with a single Docker command (bundled with Python 3.12, yt-dlp, and FFmpeg).
- **Mounted Volume**: All converted MP3s are automatically saved to your computer's local `./downloads/` folder.
- **Streamlit Web UI**:
  - Input any YouTube link.
  - In-browser audio player to listen right after conversion.
  - Download button to save files directly to your browser.
  - List of all converted files with sizes and modification times.
- **Tkinter Desktop GUI**:
  - Standalone native Windows desktop application with folder browser.
- **CLI Support**:
  - Direct conversion via command-line interface.

---

## 🐳 Running with Docker (Recommended)

No need to install Python or FFmpeg! Just start Docker Desktop and run:

### Method 1: Windows 1-Click Launchers
- **Start the app**: Double-click **`docker_start.bat`** (builds/starts the container and opens `http://localhost:8501` in your browser).
- **Stop the app**: Double-click **`docker_stop.bat`**.

### Method 2: Docker Compose CLI
```bash
# Build and start container in the background
docker-compose up -d --build
```
Access the application at: **`http://localhost:8501`**

All downloaded MP3 files will automatically appear in your local `downloads/` folder because it is mapped via a Docker volume:
```yaml
volumes:
  - ./downloads:/app/downloads
```

To stop:
```bash
docker-compose down
```

### Method 3: Standard Docker CLI
```bash
# 1. Build the image
docker build -t yt-to-mp3-app .

# 2. Run the container with local downloads folder mounted
docker run -d --name yt_mp3_converter -p 8501:8501 -v "${PWD}/downloads:/app/downloads" yt-to-mp3-app
```

---

## 💻 Running Locally (Without Docker)

### Prerequisites
1. **Python 3.10+**
2. **FFmpeg**: Ensure `ffmpeg.exe` is in your system `PATH`.
   - On Windows: `winget install Gyan.FFmpeg`

### Installation
```bash
git clone https://github.com/maheshboj/youtube-to-mp3-converter.git
cd youtube-to-mp3-converter
pip install -r requirements.txt
```

### Execution Options
- **Streamlit Web App**:
  ```bash
  streamlit run streamlit_app.py
  ```
  *(Or double-click `run_streamlit.bat`)*

- **Tkinter Desktop GUI**:
  ```bash
  python app.py
  ```
  *(Or double-click `run_app.bat`)*

- **CLI Direct Command**:
  ```bash
  python app.py "https://youtu.be/eShagnIgvZA?si=bJKHR-u97jbgojrd" "./downloads"
  ```

---

## 📁 Project Structure

```text
├── Dockerfile          # Multi-stage container recipe with FFmpeg + Python
├── docker-compose.yml  # Compose file with host volume mount for ./downloads
├── .dockerignore       # Docker ignore rules
├── docker_start.bat    # 1-click Windows Docker starter
├── docker_stop.bat     # 1-click Windows Docker stopper
├── streamlit_app.py    # Streamlit web application
├── app.py              # Tkinter desktop GUI & CLI converter
├── run_streamlit.bat   # Windows one-click local runner
├── run_app.bat         # Windows one-click desktop runner
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules for media files & cache
└── README.md           # Documentation
```
