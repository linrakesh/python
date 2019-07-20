from __future__ import unicode_literals
import youtube_dl
import urllib
import shutil
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=a8aDcLk4vRc&list=PLeo1K3hjS3uset9zIVzJWqplaWBiacTEU&index=2'])