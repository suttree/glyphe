#!/usr/bin/env python3

dir = '/home/pi/src/glyphe/'

import os, random
from PIL import Image
icons = random.sample(os.listdir(dir + 'icons/'), 4)

total_width = 1947 # to make this 400/300 on resize
total_height = 1460 # 2 * 700 + 60

new_image = Image.new('RGBA', (total_width, total_height), (255, 255, 255))

offset = (100, 20)
new_image.paste( Image.open(dir + 'icons/' + str(icons[0])), offset )

offset = ( new_image.width - 800, 20 )
new_image.paste( Image.open(dir + 'icons/' + icons[1]), offset )

offset = (100, int(new_image.height / 2) + 20)
new_image.paste( Image.open(dir + 'icons/' + icons[2]), offset )

offset = ( new_image.width - 800, int(new_image.height / 2) + 20 )
new_image.paste( Image.open(dir + 'icons/' + icons[3]), offset )

new_image.convert('P')
new_image.save(dir + 'saved/glyphe.png')

# Now resize the image to 400x300 and save it for eink display
img = Image.open(dir + 'saved/glyphe.png')
img = img.resize((400, 300), resample=Image.LANCZOS)
img = img.quantize() 

from inky import InkyWHAT
inky_display = InkyWHAT("black")
inky_display.set_border(inky_display.WHITE)

inky_display.set_image(img)
inky_display.show() 

img.save(dir + 'saved/glyphe-resized.png')
