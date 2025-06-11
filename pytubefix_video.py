from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
import subprocess
import datetime

url="https://www.youtube.com/link"

print(datetime.datetime.now())
yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

ys=yt.streams.get_highest_resolution()
ys.download()
print(datetime.datetime.now())