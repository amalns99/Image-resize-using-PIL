import sys
import os
from PIL import Image, ImageFilter


image_folder = sys.argv[1]
out_folder = sys.argv[2]


if not os.path.exists(out_folder):
    os.makedirs(out_folder)

max_ratio = (100, 100)
for item in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{item}')
    clean_name = os.path.splitext(item)[0]
    img.thumbnail(max_ratio)
    img.save(f'{out_folder}{clean_name}.png', 'png')

print('done!')
