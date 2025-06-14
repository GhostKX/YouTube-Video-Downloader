import yt_dlp

# 🔗 Ask user for a YouTube video URL
url = input("🎥 Enter YouTube URL: ").strip()

# 🔧 Configurable download target
TARGET_RESOLUTION = "1080"  # ⬆️ Max resolution
OUTPUT_FILENAME = "video_%(title).40s.%(ext)s"  # 🎯 Output file format (limited to 40 chars for safety)

# ⚙️ yt_dlp download options
ydl_opts = {
    'format': f'bestvideo[height<={TARGET_RESOLUTION}][ext=mp4][vcodec^=avc1]+bestaudio[ext=m4a]/best',
    'outtmpl': OUTPUT_FILENAME,
    'merge_output_format': 'mp4',
    'quiet': False,
    'noplaylist': True,
    'postprocessors': [
        {'key': 'FFmpegMetadata'},     # 🏷️ Embed metadata (title, author, etc.)
        {'key': 'EmbedThumbnail'},     # 🖼️ Embed thumbnail if available
    ],
}

# 🚀 Download execution
try:
    print("⬇️ Downloading video (up to 1080p, MP4, H.264)...\n")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("\n✅ Download completed successfully!")
    print("📂 Video saved with metadata and thumbnail (if available).")

except Exception as e:
    print(f"\n❌ Error occurred:\n{e}")
