#! /usr/bin/env python3

dir = '/home/pi/src/glyphe/'

import os, random
from PIL import Image
icons = random.sample(os.listdir(dir + 'icons/'), 3)
print(icons)

# The inkyphat dimensions are 212x104
# We'll stack three 700px in a line to create a 2100x1030 canvas, and resize that down later
total_width = 2100
total_height = 1030

new_image = Image.new('RGBA', (total_width, total_height), (255, 255, 255))

offset = (0, 0)
new_image.paste( Image.open(dir + 'icons/' + str(icons[0])), offset )

offset = (700, 0)
new_image.paste( Image.open(dir + 'icons/' + icons[1]), offset )

offset = (1400, 0) 
new_image.paste( Image.open(dir + 'icons/' + icons[2]), offset )

new_image.convert('P')
new_image.save(dir + 'saved/glyphe.png')

# Now resize the image to 400x300 and save it for eink display
img = Image.open(dir + 'saved/glyphe.png')
img = img.resize((212, 104), resample=Image.LANCZOS)
img = img.quantize() 
img.save(dir + 'saved/glyphe-resized.png')

from inky import InkyPHAT
inky_display = InkyPHAT("black")
inky_display.set_border(inky_display.WHITE)

inky_display.set_image(img)
inky_display.show() 

