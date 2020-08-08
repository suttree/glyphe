#!/usr/bin/env python3

import os, random
from PIL import Image
icons = random.sample(os.listdir("./icons/"), 4)
print(icons)

total_width = 1947 # to make this 400/300 on resize
total_height = 1460 # 2 * 700 + 60

new_image = Image.new('RGBA', (total_width, total_height), (220, 220, 220))

offset = (20, 20)
new_image.paste( Image.open('./icons/' + icons[0]), offset )

offset = ( int(new_image.width / 2) + 253, 20 )
new_image.paste( Image.open('./icons/' + icons[1]), offset )

offset = (20, int(new_image.height / 2) + 20)
new_image.paste( Image.open('./icons/' + icons[2]), offset )

offset = ( int(new_image.width / 2) + 253, int(new_image.height / 2) + 20 )
new_image.paste( Image.open('./icons/' + icons[3]), offset )

new_image.convert('P')
new_image.save('glyphe.png')

img = Image.open('./glyphe.png')
w, h = img.size

h_new = 300
w_new = int((float(w) / h) * h_new)
w_cropped = 400

img = img.resize((w_new, h_new), resample=Image.LANCZOS)

x0 = (w_new - w_cropped) / 2
x1 = x0 + w_cropped
y0 = 0
y1 = h_new

img = img.crop((x0, y0, x1, y1))

pal_img = Image.new("P", (1, 1))
pal_img.putpalette((255, 255, 255, 0, 0, 0, 255, 0, 0) + (0, 0, 0) * 252)

#img = img.convert("RGB").quantize(palette=pal_img)
img = img.quantize() 

from inky import InkyWHAT
inky_display = InkyWHAT("black")
inky_display.set_border(inky_display.WHITE)

inky_display.set_image(img)
inky_display.show() 

img.save('glyphe-resized.png')
