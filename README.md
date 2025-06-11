# 🎬 YouTube Downloader Scripts Collection

A **powerful collection of Python scripts** for downloading YouTube videos and audio using two popular libraries: **pytubefix** and **yt-dlp**. Choose from **8 specialized scripts** designed for different download scenarios - from high-quality video downloads to audio-only extractions.

Built with **robust error handling**, **automatic codec optimization**, and **clean file management**, these scripts provide **reliable YouTube content downloading** with comprehensive progress tracking.

---

## ✨ Features

### 🎵 Audio Downloads
- **High-Quality MP3 Audio Extraction** from YouTube videos
- **Automatic Format Conversion** (M4A to MP3)
- **Bitrate Optimization** for best audio quality
- **Progress Tracking** during downloads
- **Clean Temporary File Management**

### 🎬 Video Downloads
- **Multiple Quality Options** - from standard to 4K resolution
- **Smart Codec Detection** - avoids unnecessary re-encoding
- **Separate Audio/Video Streams** for maximum quality
- **H.264 Compatibility Optimization**
- **Adaptive Stream Processing**

### 🔧 Advanced Processing
- **FFmpeg Integration** for professional-grade conversion
- **Automatic Codec Optimization**
- **Batch Processing Capabilities**
- **Resolution-Specific Downloads**
- **Metadata Preservation**

### 🛡️ Reliability Features
- **Robust Exception Handling**
- **Automatic File Cleanup**
- **Progress Monitoring**
- **Codec Compatibility Checks**
- **Download Verification**

---

## 🔧 Requirements

### System Dependencies
- **Python 3.8+**
- **FFmpeg** (for audio/video processing)
- **Stable Internet Connection**

### Python Libraries
```
pytubefix==8.13.1
yt-dlp==2025.6.9
```

---

## 🚀 Installation

### 1. Clone or Download the Scripts
```bash
git clone <YouTube-Video-Downloader>
cd YouTube-Video-Downloader
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Install FFmpeg

#### Ubuntu/Debian:
```bash
sudo apt update
sudo apt install ffmpeg
```

#### macOS:
```bash
brew install ffmpeg
```

#### Windows:
Download from [FFmpeg official website](https://ffmpeg.org/download.html) and add to PATH.

### 4. Verify FFmpeg Installation
```bash
ffmpeg -version
```

### 5. Configure Your YouTube URL
Edit the script you want to use and replace the placeholder URL:
```python
url = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
```

### 6. Run Your Chosen Script
```bash
python script_name.py
```

---

## 📱 Script Overview

### 🎵 PyTubeFix Audio Scripts

#### **`pytubefix_audio_only.py`** - Premium Audio Extraction
- **Downloads** highest quality audio stream
- **Converts** to MP3 with premium quality settings
- **Output**: `final_audio.mp3`
- **Features**: Automatic codec optimization, temporary file cleanup

### 🎬 PyTubeFix Video Scripts

#### **`pytubefix_video.py`** - Quick Video Download
- **Downloads** highest resolution available
- **Simple & Fast** - perfect for quick downloads
- **Output**: Original YouTube filename
- **Features**: Direct download, no processing

#### **`pytubefix_video_hd.py`** - Professional HD Download
- **Downloads** separate video and audio streams
- **Merges** for maximum quality
- **Smart codec detection** - avoids re-encoding when possible
- **Output**: `final_video_4.mp4`
- **Features**: Advanced processing, codec optimization

#### **`pytubefix_video_only.py`** - Video Stream Only
- **Downloads** video without audio track
- **Ensures** H.264 compatibility
- **Output**: `video_compatible.mp4`
- **Features**: Codec validation, compatibility optimization

### 🌐 yt-dlp Scripts Collection

#### **`ytdlp_audio_only.py`** - Interactive Audio Extractor
- **Prompts** for URL input
- **Extracts** best available audio
- **Direct MP3 conversion** with 192kbps quality
- **Output**: `audio_1.mp3`
- **Features**: Interactive interface, automatic format selection

#### **`ytdlp_video_hd.py`** - Best Quality Video
- **Downloads** best video with audio
- **Prefers** H.264/AAC codecs for compatibility
- **Output**: `downloaded_video.mp4`
- **Features**: Quality optimization, format preference

#### **`ytdlp_video_only.py`** - Video Stream Extraction
- **Downloads** video stream only (no audio)
- **Ensures** H.264 codec compatibility
- **Output**: `test.mp4`
- **Features**: Stream isolation, codec verification

#### **`ytdlp_video_specific.py`** - Custom Resolution Control
- **Limits** resolution to 1080p maximum
- **Embeds** metadata and thumbnails
- **Custom filename** with video title
- **Output**: `video_[TITLE].mp4`
- **Features**: Resolution control, metadata embedding

---

## 📖 Usage Guide

### Basic Usage Flow

#### 1. **Choose Your Script**
Select based on your needs:
- 🎵 **Audio only**: `pytubefix_audio_only.py` or `ytdlp_audio_only.py`
- 🎬 **Quick video**: `pytubefix_video.py`
- 🏆 **Best quality**: `pytubefix_video_hd.py` or `ytdlp_video_hd.py`
- 📱 **Specific resolution**: `ytdlp_video_specific.py`

#### 2. **Configure the URL**
```python
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

#### 3. **Run the Script**
```bash
python pytubefix_audio_only.py
```

#### 4. **Monitor Progress**
Watch the console output for download progress and processing status.

### Interactive Scripts Usage

Some yt-dlp scripts prompt for input:
```bash
python ytdlp_audio_only.py
# Enter YouTube video URL: https://www.youtube.com/watch?v=YOUR_VIDEO_ID
```

### Example Processing Flow:
```
🔍 Getting video information...
📊 Video Title: "Amazing YouTube Video"
⬇️ Downloading video stream...
🎧 Processing audio extraction...
🔄 Converting to MP3 format...
✅ Download complete: final_audio.mp3
🧹 Cleaning up temporary files...
✅ Process finished successfully!
```

---

## 📊 Detailed Script Comparison

### Audio Extraction Scripts

| Script | Library | Quality | Output | Interactive | Processing Time |
|--------|---------|---------|---------|-------------|----------------|
| `pytubefix_audio_only.py` | PyTubeFix | Highest | `final_audio.mp3` | ❌ | Medium |
| `ytdlp_audio_only.py` | yt-dlp | 192kbps | `audio_1.mp3` | ✅ | Fast |

### Video Download Scripts

| Script | Library | Quality | Audio | Output | Processing |
|--------|---------|---------|--------|---------|-----------|
| `pytubefix_video.py` | PyTubeFix | Highest | ✅ | Original name | None |
| `pytubefix_video_hd.py` | PyTubeFix | Maximum | ✅ | `final_video_4.mp4` | Advanced |
| `pytubefix_video_only.py` | PyTubeFix | Highest | ❌ | `video_compatible.mp4` | H.264 check |
| `ytdlp_video_hd.py` | yt-dlp | Best | ✅ | `downloaded_video.mp4` | Smart codec |
| `ytdlp_video_only.py` | yt-dlp | Best | ❌ | `test.mp4` | Stream only |
| `ytdlp_video_specific.py` | yt-dlp | ≤1080p | ✅ | `video_[TITLE].mp4` | Metadata rich |

---

## 🔍 Advanced Features

### Smart Codec Detection
Scripts automatically detect video/audio codecs and optimize processing:
```python
if 'avc1' in video_stream.video_codec.lower():
    print("Video is already H.264 - no re-encoding needed")
    # Skip re-encoding for faster processing
else:
    print("Re-encoding to H.264 for compatibility...")
    # Apply H.264 encoding
```

### Progress Tracking
Real-time download progress with detailed information:
```
🔍 Getting the video stream...
🎵 Getting the audio stream...
⬇️ Downloading video stream... [████████████████████] 100%
⬇️ Downloading audio stream... [████████████████████] 100%
🔄 Processing and merging streams...
```

### Automatic Cleanup
All scripts include comprehensive cleanup procedures:
- ✅ **Remove temporary files**
- ✅ **Handle processing errors**
- ✅ **Verify successful downloads**
- ✅ **Clean up on interruption**

---

## 📊 Performance Optimization

### Speed vs Quality Trade-offs

#### **Fastest Download** ⚡
- Use: `pytubefix_video.py`
- **Pros**: Direct download, no processing
- **Cons**: May not be highest quality

#### **Best Quality** 🏆
- Use: `pytubefix_video_hd.py` or `ytdlp_video_specific.py`
- **Pros**: Maximum quality, metadata preservation
- **Cons**: Longer processing time

#### **Balanced Approach** ⚖️
- Use: `ytdlp_video_hd.py`
- **Pros**: Good quality, reasonable speed
- **Cons**: Some processing overhead

---

## 📄 File Output Reference

| Script | Output File | Format | Quality | Audio | Size |
|--------|-------------|--------|---------|--------|------|
| `pytubefix_audio_only.py` | `final_audio.mp3` | MP3 | High | ✅ | Small |
| `ytdlp_audio_only.py` | `audio_1.mp3` | MP3 | 192kbps | ✅ | Small |
| `pytubefix_video.py` | Original name | MP4 | Highest | ✅ | Large |
| `pytubefix_video_hd.py` | `final_video_4.mp4` | MP4 | Maximum | ✅ | Largest |
| `pytubefix_video_only.py` | `video_compatible.mp4` | MP4 | High | ❌ | Medium |
| `ytdlp_video_hd.py` | `downloaded_video.mp4` | MP4 | Best | ✅ | Large |
| `ytdlp_video_only.py` | `test.mp4` | MP4 | Best | ❌ | Medium |
| `ytdlp_video_specific.py` | `video_[TITLE].mp4` | MP4 | ≤1080p | ✅ | Variable |

---

## 👨‍💻 Author

Developed by **GhostKX**

- 🌐 **GitHub**: [@GhostKX](https://github.com/GhostKX)