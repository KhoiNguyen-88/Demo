import os

from PIL import Image
import glob
#i = 0
#image_list = []
for filename in glob.glob('/home/nguyen/Desktop/python/Pics/*.jpg'):
    im = Image.open(filename,'r')
    #image_list.append(im)
    im.read()
