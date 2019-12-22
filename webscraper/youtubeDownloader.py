from __future__ import unicode_literals
import youtube_dl
# import urllib
# import shutil
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(
        ['https://www.youtube.com/watch?v=7nH2NYpeKa4&list=PLuiqR73XWRBZ7PpaADMES1LCtvzkc2MJt&index=1'])
