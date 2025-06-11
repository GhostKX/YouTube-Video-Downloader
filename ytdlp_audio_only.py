import yt_dlp

url = input("Enter YouTube video URL: ")

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'audio_1.%(ext)s',
    'noplaylist': True,
    'quiet': False,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
