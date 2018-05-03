from __future__ import unicode_literals
import youtube_dl
import urllib
import shutil
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/playlist?list=PLgPJX9sVy92yWUMgLpWrXtegKxrWLRnRv'])