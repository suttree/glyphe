#!/usr/bin/env python

dir = '/home/pi/src/glyphe/'

import os, random
from PIL import Image
icons = random.sample(os.listdir(dir + 'icons/'), 4)
print(icons)

total_width = 1947 # to make this 400/300 on resize
total_height = 1460 # 2 * 700 + 60

new_image = Image.new('RGBA', (total_width, total_height), (255, 255, 255))

offset = ( int(total_width / 2) - 700, 30)
new_image.paste( Image.open(dir + 'icons/' + str(icons[0])), offset )

offset = ( int(total_width / 2), 30 )
new_image.paste( Image.open(dir + 'icons/' + icons[1]), offset )

offset = ( int(total_width / 2) - 700, int(new_image.height / 2) + 10)
new_image.paste( Image.open(dir + 'icons/' + icons[2]), offset )

offset = ( int(new_image.width / 2), int(new_image.height / 2) + 10 )
new_image.paste( Image.open(dir + 'icons/' + icons[3]), offset )

new_image.convert('P')
new_image.save(dir + 'saved/glyphe.png')

# Now resize the image to 400x300 and save it for eink display
img = Image.open(dir + 'saved/glyphe.png')
img = img.resize((400, 300), resample=Image.LANCZOS)
img = img.quantize() 
img.save(dir + 'saved/glyphe-resized.png')

from inky import InkyWHAT
inky_display = InkyWHAT("black")
inky_display.set_border(inky_display.WHITE)

#inky_display.clear()
inky_display.set_image(img)
inky_display.show() 
