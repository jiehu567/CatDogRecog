# -*- coding: utf-8 -*-
"""
Batch Resize Image in a directory

"""
import os
from PIL import Image
from resizeimage import resizeimage

# Get filenames in a list
origin_path = raw_input("input directory of ORIGINAL images: ")
output_path = raw_input("input directory of PROCESSED images: ")

if not os.path.exists(output_path):
    os.makedirs(output_path)

from os import listdir
from os.path import isfile, join

filenames = [f for f in listdir(origin_path) if isfile(join(origin_path, f))]


for file in filenames:
    with open(origin_path + '/' + file, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [32, 32])
            cover.save(output_path + '/32_32_' + file)

