@echo off
cd /d "%~dp0"
echo Stopping YouTube to MP3 Converter container...
docker-compose down
docker stop yt_mp3_converter 2>nul
docker rm yt_mp3_converter 2>nul
echo Done.
pause
