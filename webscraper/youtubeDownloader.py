from __future__ import unicode_literals
import youtube_dl
import urllib
import shutil
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['http://103.67.198.6/uploaded-videos/The.Raid.2.2014.1080p.BluRay.x264-YTS.AG.MP4'])