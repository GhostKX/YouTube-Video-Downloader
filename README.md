# <a href="https://youtube.com" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png" width="28" valign="middle"/></a> YouTube Video Downloader

<div align="center">

[![YouTube Downloader](https://img.shields.io/badge/YouTube-Downloader-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![License](https://img.shields.io/badge/License-Educational-green?style=for-the-badge)](https://creativecommons.org/licenses/by-nd/4.0/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge&logo=opensourceinitiative&logoColor=black)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)](https://github.com/GhostKX/YouTube-Video-Downloader)

**Professional-Grade YouTube Content Downloading Toolkit**

*A comprehensive collection of 8 specialized Python scripts for downloading YouTube videos and audio with enterprise-level reliability and HD quality optimization.*

[🚀 Quick Start](#-quick-start) • [📱 Scripts Overview](#-scripts-overview) • [🛠️ Installation](#-installation) • [📖 Usage Guide](#-usage-guide) • [🔧 Features](#-advanced-features)

---

</div>

## ✨ Key Features

<table>
<tr>
<th width="25%">🎯 Feature</th>
<th width="25%">🎵 Audio Extraction</th>
<th width="25%">🎬 Video Downloads</th>
<th width="25%">🔧 Advanced Processing</th>
</tr>
<tr>
<td><strong>Quality Options</strong></td>
<td>192kbps MP3, High-Quality</td>
<td>Standard to 4K, HD/Ultra HD</td>
<td>Codec Optimization, FFmpeg</td>
</tr>
<tr>
<td><strong>Libraries</strong></td>
<td>PyTubeFix, yt-dlp</td>
<td>PyTubeFix, yt-dlp</td>
<td>Both Libraries</td>
</tr>
<tr>
<td><strong>Output Formats</strong></td>
<td>MP3, M4A</td>
<td>MP4, Original</td>
<td>Optimized MP4/MP3</td>
</tr>
<tr>
<td><strong>Special Features</strong></td>
<td>Auto Conversion</td>
<td>Stream Merging</td>
<td>Smart Codec Detection</td>
</tr>
</table>

### 🏆 **Why Choose This Toolkit?**
- **8 Specialized Scripts** - Each optimized for specific download scenarios
- **Dual-Library Support** - PyTubeFix and yt-dlp for maximum compatibility
- **HD Quality Processing** - Automatic codec optimization with FFmpeg
- **Zero Configuration** - Works out of the box with minimal setup
- **Robust Error Handling** - Built-in retry mechanisms and cleanup

---

## 🚀 Quick Start

### ⚡ **30-Second Setup**

```bash
# 1. Clone and navigate
git clone https://github.com/your-repo/youtube-downloader.git
cd youtube-downloader

# 2. Install dependencies
pip install -r requirements.txt

# 3. Install FFmpeg (required)
# Ubuntu/Debian: sudo apt install ffmpeg
# macOS: brew install ffmpeg
# Windows: Download from ffmpeg.org

# 4. Start downloading
python pytubefix_video.py
```

### 🎯 **Choose Your Script**

| Script | Perfect For | Speed | Quality | Library |
|--------|-------------|-------|---------|---------|
| **`pytubefix_video.py`** | Quick video downloads | ⚡⚡⚡ | High | PyTubeFix |
| **`pytubefix_video_hd.py`** | Maximum quality video | ⚡⚡ | Ultra HD | PyTubeFix |
| **`pytubefix_audio_only.py`** | Premium audio extraction | ⚡⚡ | High MP3 | PyTubeFix |
| **`ytdlp_video_hd.py`** | Best quality with compatibility | ⚡⚡ | HD | yt-dlp |
| **`ytdlp_audio_only.py`** | Interactive audio download | ⚡⚡⚡ | 192kbps | yt-dlp |
| **`ytdlp_video_specific.py`** | Custom resolution control | ⚡⚡ | ≤1080p | yt-dlp |

---

## 📱 Scripts Overview

### 🎵 **Audio Extraction Scripts**

<details>
<summary><strong>🎧 pytubefix_audio_only.py</strong> - Premium Audio Extraction</summary>

**🎯 Perfect for**: Music lovers, high-quality audio extraction

**✨ Key Features**:
- 🎵 Highest quality audio stream download
- 🔄 Automatic MP3 conversion with premium quality
- 🧹 Automatic temporary file cleanup
- 📊 Progress tracking during conversion

**Usage**:
```python
# Edit the script
url = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
python pytubefix_audio_only.py
```

**Output**: `final_audio.mp3`

</details>

<details>
<summary><strong>🎶 ytdlp_audio_only.py</strong> - Interactive Audio Extractor</summary>

**🎯 Perfect for**: Quick audio extraction, interactive use

**✨ Key Features**:
- 💬 Interactive URL input
- ⚡ Direct MP3 conversion (192kbps)
- 🔄 Automatic format selection
- 📱 User-friendly interface

**Interactive Flow**:
```bash
python ytdlp_audio_only.py
📥 Enter YouTube video URL: [paste_url_here]
🎧 Extracting and converting to MP3...
✅ Success! Audio saved as: audio_1.mp3
```

</details>

### 🎬 **Video Download Scripts**

<details>
<summary><strong>📹 pytubefix_video.py</strong> - Quick Video Download</summary>

**🎯 Perfect for**: Fast downloads, original quality

**✨ Key Features**:
- ⚡ Lightning-fast direct downloads
- 🎬 Highest available resolution
- 📁 Original YouTube filename preserved
- 🔄 No additional processing overhead

**Usage**:
```python
url = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
python pytubefix_video.py
```

</details>

<details>
<summary><strong>🏆 pytubefix_video_hd.py</strong> - Professional HD Download</summary>

**🎯 Perfect for**: Maximum quality, professional use

**✨ Key Features**:
- 🎬 Separate video and audio stream downloads
- 🔧 Smart codec detection and optimization
- 📱 H.264 compatibility assurance
- 💾 Advanced stream merging

**Processing Pipeline**:
```
🔍 Getting video and audio streams...
⬇️ Downloading video stream...
⬇️ Downloading audio stream...
🔄 Smart codec processing...
✅ HD video ready: final_video_4.mp4
```

</details>

<details>
<summary><strong>🌐 ytdlp_video_hd.py</strong> - Best Quality with Compatibility</summary>

**🎯 Perfect for**: Reliable downloads, codec preference

**✨ Key Features**:
- 🎯 Best video with audio combined
- 🔧 H.264/AAC codec preference
- 🛡️ Enhanced compatibility
- 📊 Quality optimization

**Output**: `downloaded_video.mp4`

</details>

<details>
<summary><strong>🎛️ ytdlp_video_specific.py</strong> - Custom Resolution Control</summary>

**🎯 Perfect for**: Bandwidth control, specific requirements

**✨ Key Features**:
- 📐 Resolution limit (≤1080p)
- 🏷️ Metadata and thumbnail embedding
- 📝 Custom filename with video title
- 🎯 Optimized file size management

**Output**: `video_[TITLE].mp4`

</details>

### 🎥 **Video-Only Scripts**

<details>
<summary><strong>📺 pytubefix_video_only.py & ytdlp_video_only.py</strong> - Stream Isolation</summary>

**🎯 Perfect for**: Video-only content, audio separation

**✨ Key Features**:
- 🎬 Video stream without audio track
- 🔧 H.264 codec compatibility verification
- 📱 Mobile-friendly format optimization
- 💾 Reduced file sizes

</details>

---

## 🛠️ Installation

### 📋 **System Requirements**

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **Python** | 3.8+ | 3.10+ |
| **FFmpeg** | Latest | Latest |
| **RAM** | 2GB | 4GB+ |
| **Storage** | 1GB | 5GB+ |
| **Internet** | 5 Mbps | 25+ Mbps |

### 🔧 **Step-by-Step Installation**

#### **1. Environment Setup**
```bash
# Create virtual environment (recommended)
python -m venv youtube_downloader
source youtube_downloader/bin/activate  # Linux/Mac
youtube_downloader\Scripts\activate     # Windows
```

#### **2. Install Python Dependencies**
```bash
# Install required packages
pip install -r requirements.txt

# Verify installation
python -c "import pytubefix, yt_dlp; print('✅ All packages ready!')"
```

#### **3. Install FFmpeg (Critical)**

**Windows:**
```powershell
# Download from https://ffmpeg.org/download.html
# Add to system PATH
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install ffmpeg
```

#### **4. Verify Complete Installation**
```bash
# Test all components
python -c "
import sys, pytubefix, yt_dlp, subprocess
print('✅ Python:', sys.version[:5])
print('✅ PyTubeFix: Ready')
print('✅ yt-dlp:', yt_dlp.version.__version__)
subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
print('✅ FFmpeg: Ready')
print('🎉 Installation Complete!')
"
```

---

## 📖 Usage Guide

### 🎯 **Common Scenarios**

#### **Scenario 1: Download Music Video as Audio**
```bash
# 1. Copy YouTube URL
# 2. Edit pytubefix_audio_only.py:
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# 3. Run script
python pytubefix_audio_only.py
```

#### **Scenario 2: Download HD Video**
```bash
# For maximum quality
python pytubefix_video_hd.py

# For compatibility and speed
python ytdlp_video_hd.py
```

#### **Scenario 3: Interactive Download**
```bash
# Interactive audio extraction
python ytdlp_audio_only.py
# Paste URL when prompted
```

### 📁 **File Organization**

```
YouTube-Downloads/
├── Audio/                       # Audio extractions
│   ├── final_audio.mp3         # PyTubeFix audio
│   └── audio_1.mp3             # yt-dlp audio
├── Video/                      # Video downloads
│   ├── final_video_4.mp4       # HD processed
│   ├── downloaded_video.mp4    # yt-dlp HD
│   └── video_[TITLE].mp4       # Custom named
└── VideoOnly/                  # Video-only streams
    ├── video_compatible.mp4    # PyTubeFix
    └── test.mp4               # yt-dlp
```

---

## 🔍 Advanced Features

### 🧠 **Smart Codec Detection**
```python
# Automatic codec optimization
if 'avc1' in video_stream.video_codec.lower():
    print("✅ Video is already H.264 - no re-encoding needed")
else:
    print("🔄 Re-encoding to H.264 for compatibility...")
```

### 📊 **Progress Tracking**
```
🔍 Getting video information...
📊 Video Title: "Amazing YouTube Video"
⬇️ Downloading video stream... [████████████████████] 100%
🎧 Processing audio extraction...
🔄 Converting to MP3 format...
✅ Download complete!
```

### 🧹 **Automatic Cleanup**
- ✅ Remove temporary files
- ✅ Handle processing errors
- ✅ Verify successful downloads
- ✅ Clean up on interruption

---

## 📊 Performance Benchmarks

| Content Type | File Size | Processing Time | Quality |
|-------------|-----------|-----------------|---------|
| Audio Only | 3-8 MB | 5-15 seconds | 192kbps+ |
| Standard Video | 50-200 MB | 10-30 seconds | 720p-1080p |
| HD Video | 100-500 MB | 15-45 seconds | 1080p-4K |
| Video Only | 40-150 MB | 8-25 seconds | No Audio |

---

## 📊 Script Comparison Table

| Script | Library | Output | Quality | Audio | Processing | Best For |
|--------|---------|--------|---------|--------|-----------|----------|
| `pytubefix_audio_only.py` | PyTubeFix | `final_audio.mp3` | High | ✅ | Medium | Music extraction |
| `ytdlp_audio_only.py` | yt-dlp | `audio_1.mp3` | 192kbps | ✅ | Fast | Quick audio |
| `pytubefix_video.py` | PyTubeFix | Original name | Highest | ✅ | None | Fast download |
| `pytubefix_video_hd.py` | PyTubeFix | `final_video_4.mp4` | Maximum | ✅ | Advanced | Max quality |
| `pytubefix_video_only.py` | PyTubeFix | `video_compatible.mp4` | High | ❌ | H.264 check | Video only |
| `ytdlp_video_hd.py` | yt-dlp | `downloaded_video.mp4` | Best | ✅ | Smart codec | Reliable |
| `ytdlp_video_only.py` | yt-dlp | `test.mp4` | Best | ❌ | Stream only | No audio |
| `ytdlp_video_specific.py` | yt-dlp | `video_[TITLE].mp4` | ≤1080p | ✅ | Metadata rich | Custom size |

---

## 🔍 Troubleshooting

### ❌ **Common Issues**

**FFmpeg Not Found:**
```bash
# Solution: Install FFmpeg and add to PATH
ffmpeg -version
```

**Download Failed:**
```bash
# Solution: Update libraries
pip install --upgrade pytubefix yt-dlp
```

**Codec Issues:**
```bash
# Solution: Ensure FFmpeg is properly installed
# Check codec availability: ffmpeg -codecs
```

**Network Errors:**
```bash
# Solution: Check internet connection and YouTube URL
# Verify URL is accessible in browser
```

---

## 📊 Dependencies

### **Core Requirements** (`requirements.txt`)
```
pytubefix==8.13.1
yt-dlp==2025.6.9
```

### **System Dependencies**
- **Python 3.8+**: Core runtime
- **FFmpeg**: Essential for audio/video processing
- **Stable Internet**: Download reliability

---

## 🔒 Privacy & Legal

### **Best Practices**
- ✅ Only download content you have permission to access
- ✅ Respect YouTube's Terms of Service
- ✅ Use for personal purposes only
- ✅ Support content creators through official channels

### **Educational Use**
This project is for **educational purposes only**. Please respect YouTube's Terms of Service and only download content you have permission to access.

---

## 📜 License

This project is for **educational purposes only**. Please respect YouTube's Terms of Service and only download content you have permission to access.

---

## ⭐ Acknowledgments

- **PyTubeFix team** for excellent YouTube downloading capabilities
- **yt-dlp contributors** for robust video processing functionality
- **FFmpeg project** for powerful multimedia processing tools

---

<div align="center">

## 👨‍💻 Author

Developed by **GhostKX**

🌐 **GitHub**: [@GhostKX](https://github.com/GhostKX)

</div>