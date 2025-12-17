# yt-dlp + FFmpeg

## Python version

Written and tested using **Python 3.12.7**.

## Python dependencies

Install required packages:
pip install yt-dlp certifi

## FFmpeg installation (Windows)

1. Download FFmpeg:
https://www.gyan.dev/ffmpeg/builds/

Download:
ffmpeg-release-essentials.zip

2. Extract files to:
C:\ffmpeg\bin\

Required files:
C:\ffmpeg\bin\ffmpeg.exe
C:\ffmpeg\bin\ffprobe.exe
C:\ffmpeg\bin\ffplay.exe

3. Add to Windows PATH:
C:\ffmpeg\bin

4. Verify:
ffmpeg -version

## Windows certificate handling

Due to a **Windows-specific certificate validation problem**, SSL certificate checking is disabled in the  code with  "nocheckcertificate": True 

## macOS note

On macOS, the application works without disabling SSL certificate verification and does not require any certificate-related workaround.


## Python script

```python
import yt_dlp

url = input("Enter video URL: ").strip()

ydl_opts = {
    "format": "bestvideo*+bestaudio/best",
    "merge_output_format": "mp4",
    "ffmpeg_location": r"C:\ffmpeg\bin",
    "nocheckcertificate": True
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download completed.")

