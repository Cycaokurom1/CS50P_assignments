import sys
from PIL import Image, ImageOps
from os import path

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
elif not sys.argv[1].endswith('jpg') and not sys.argv[1].endswith('jpeg') and not sys.argv[1].endswith('png'):
    sys.exit('Invalid input')
elif not sys.argv[2].endswith('jpg') and not sys.argv[2].endswith('jpeg') and not sys.argv[2].endswith('png'):
    sys.exit('Invalid input')

root1, ext1 = path.splitext(sys.argv[1])
root2, ext2 = path.splitext(sys.argv[2])

if ext1 != ext2:
    sys.exit('Input and output have different extensions')

try:
    background = Image.open(sys.argv[1])
    shirt = Image.open('shirt.png')
    resized_bg = ImageOps.fit(background, shirt.size)
    resized_bg.paste(shirt, shirt)
    resized_bg.save(sys.argv[2])
except FileNotFoundError:
    sys.exit('File does not exist')