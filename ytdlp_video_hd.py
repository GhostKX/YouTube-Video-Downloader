import yt_dlp

# 🔗 Prompt the user for a YouTube video URL
url = input("🎥 Enter YouTube video URL: ").strip()

# ⚙️ yt_dlp options
ydl_opts = {
    'format': 'bestvideo[ext=mp4][vcodec^=avc1]+bestaudio[ext=m4a]/best',  # 🎞️ Prefer H.264 video + AAC audio
    'outtmpl': 'downloaded_video.%(ext)s',        # 💾 Output filename (e.g. .mp4)
    'merge_output_format': 'mp4',                 # 🧩 Merge into MP4
    'noplaylist': True,                           # 🚫 Only download a single video
    'quiet': False,                               # 📢 Show download progress
    'verbose': True,                              # 🧾 Show debug info (optional)
}

# 🚀 Download process
try:
    print("⬇️ Downloading and processing video...\n")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("\n✅ Download complete!")

except Exception as e:
    print(f"\n❌ An error occurred:\n{e}")

