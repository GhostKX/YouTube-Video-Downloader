import yt_dlp

url = input("Enter YouTube URL: ")

TARGET_RESOLUTION = "1080"
OUTPUT_FILENAME = "video_%(title)s.%(ext)s"

ydl_opts = {
    'format': f'bestvideo[height<={TARGET_RESOLUTION}][ext=mp4][vcodec^=avc1]+bestaudio[ext=m4a]/best',
    'outtmpl': OUTPUT_FILENAME,
    'merge_output_format': 'mp4',
    'quiet': False,
    'noplaylist': True,
    'postprocessors': [
        {'key': 'FFmpegMetadata'},
        {'key': 'EmbedThumbnail'},
    ],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])