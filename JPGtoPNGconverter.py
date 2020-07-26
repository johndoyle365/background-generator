# images with just a few colours are actually better when you develop websites to use PNG
from PIL import Image, ImageFilter
from sys import argv
import os

try:
    orig_img_folder = argv[1]
    new_folder = argv[2]

    img_files = os.listdir(orig_img_folder)

    if not os.path.exists(new_folder):  # could also use pathlib module for this
        os.mkdir(new_folder)

    for filename in img_files:
        img = Image.open(f'{orig_img_folder}{filename}')
        clean_name = os.path.splitext(filename)[0]
        img.save(f'{new_folder}{clean_name}.png', 'png')

except IndexError as err:
    print(f'Please use command format \"python JPGtoPNGconverter.py source_dir/ new_dir/\"')
