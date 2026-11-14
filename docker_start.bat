@echo off
cd /d "%~dp0"
echo Starting YouTube to MP3 Converter with Docker...
docker-compose up -d --build
if %ERRORLEVEL% EQU 0 (
    echo App started successfully!
    echo Opening http://localhost:8501 ...
    start http://localhost:8501
) else (
    echo Failed to start with docker-compose. Trying docker build and run...
    docker build -t yt-to-mp3-app .
    docker run -d --name yt_mp3_converter -p 8501:8501 -v "%cd%\downloads:/app/downloads" yt-to-mp3-app
    start http://localhost:8501
)
pause
