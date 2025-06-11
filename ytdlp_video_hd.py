import yt_dlp
import datetime

url = input("Enter YouTube video URL: ")

ydl_opts = {
    'format': 'bestvideo[ext=mp4][vcodec^=avc1]+bestaudio[ext=m4a]/best',
    'outtmpl': 'downloaded_video.%(ext)s',
    'merge_output_format': 'mp4',
    'noplaylist': True,
    'quiet': False,
    'verbose': True,
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

