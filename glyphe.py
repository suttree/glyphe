#!/usr/bin/env python

import os, sys, random, getopt, pickle
from PIL import Image

dir = '/home/pi/src/glyphe/' + random.sample(['dark', 'light'], 1)[0] + '/'

def setup():
  pickle.dump( random.sample(os.listdir(dir + 'icons/'), 4), open( "glyphes.pickle", "wb" ) )

def glyphe():
  # Load the icons and rotate them each time. This gives us
  # a horoscope which rotates during the day, potentially 
  # making us think differently about their meaning
  print("Starting...")
  icons = pickle.load( open( "glyphes.pickle", "rb" ) )
  print(icons)
  icons.insert(0, icons.pop()) # put the last element at the front
  pickle.dump( icons, open( "glyphes.pickle", "wb" ) )
  print(icons)

  total_width = 1947 # to make this 400/300 on resize
  total_height = 1460 # 2 * 700 + 60

  new_image = Image.new('RGBA', (total_width, total_height), 255)

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

  inky_display.set_image(img)
  inky_display.show() 
  print("Done!")

def usage():
  print("glyphe.py -h (help) -s (setup)")

def main(argv):
  try:
    opts, args = getopt.getopt(argv, "hs", ['help', 'setup'])
    for opt, arg in opts:
      if opt in ("-h", "--help"):
        usage()
        sys.exit()

      if opt in ("-s", "--setup"):
        setup()

    glyphe()

  except getopt.GetoptError:
    usage()
    sys.exit(2)

if __name__ == "__main__":
  main(sys.argv[1:])