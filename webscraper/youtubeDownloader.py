from __future__ import unicode_literals
import youtube_dl
# import urllib
# import shutil
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
<<<<<<< HEAD
    ydl.download(['https://www.youtube.com/watch?v=wF_B_aagLfI'])
=======
    ydl.download(
        ['https://www.youtube.com/watch?v=SCoGwHCNXVw'])
>>>>>>> 4862d6baee53c91054712373dd7190e101b83a22
