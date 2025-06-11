import yt_dlp

url = input("Enter YouTube video URL: ")

ydl_opts = {
    'format': 'bestvideo[ext=mp4][vcodec^=avc1]',
    'outtmpl': 'test.mp4',
    'noplaylist': True,
    'quiet': False,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
