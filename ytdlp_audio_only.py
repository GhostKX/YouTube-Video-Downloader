import yt_dlp

# 🔗 Ask user to paste the YouTube video URL
url = input("🎥 Enter YouTube video URL: ").strip()

# ⚙️ Options for yt_dlp to extract and convert audio to MP3
ydl_opts = {
    'format': 'bestaudio/best',                   # 🎧 Best available audio stream
    'outtmpl': 'audio_%(title).40s.%(ext)s',      # 💾 Output filename (title trimmed to 40 chars)
    'noplaylist': True,                           # 🚫 Only download single video, not playlist
    'quiet': False,                               # 📢 Show output while downloading
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',              # 🛠️ Use ffmpeg to extract audio
        'preferredcodec': 'mp3',                  # 🎵 Output format
        'preferredquality': '192',                # 🎚️ Bitrate
    }],
}

try:
    print("\n⬇️ Starting download and conversion...\n")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("\n✅ MP3 download and conversion completed successfully!")

except Exception as e:
    print(f"\n❌ An error occurred:\n{e}")
