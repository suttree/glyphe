#!/usr/bin/env python3

import os, random
from PIL import Image

icons = random.sample(os.listdir("./icons/"), 4)
print(icons)

total_width = 700 * 2 + 20 * 3 # two 700px icons plus 20px padding on the left, right and middle
total_height = total_width # same, we want to make a square
new_image = Image.new('RGB', (total_width, total_height), (255, 255, 255))

offset = (20, 20)
new_image.paste( Image.open('./icons/' + icons[0]), offset )

offset = (new_image.width - 20, 20)
new_image.paste( Image.open('./icons/' + icons[1]), offset )

offset = (20, int(new_image.height / 2) + 20)
new_image.paste( Image.open('./icons/' + icons[2]), offset )

offset = (new_image.width - 20, int(new_image.height / 2) + 20)
new_image.paste( Image.open('./icons/' + icons[3]), offset )

new_image.save('test.png')
