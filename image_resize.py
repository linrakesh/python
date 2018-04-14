#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      acer
#
# Created:     08-02-2018
# Copyright:   (c) acer 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from PIL import Image
from resizeimage import resizeimage

with open('big.jpeg', 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [600, 400])
        cover.save('test-image-cover.jpeg', image.format)