import os
import glob

import cv2
from PIL import Image


def load_images():
    ind = 1
    for image in glob.glob("/home/aakash/Downloads/dataset/warrior1Q/*"):
        img = Image.open(image)
        img = img.convert('RGB')
        img1 = img.resize((400, 300), Image.ANTIALIAS)
        img1.save('/home/aakash/Downloads/dataset/warrior1/File' + str(ind) + '.jpg')
        ind = ind + 1
        print(ind)
    return


load_images()
