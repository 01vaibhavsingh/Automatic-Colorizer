import os
from PIL import Image
import numpy as np


def resize():
    path = 'data/landscape-test/'
    files = os.listdir(path)

    for file in files:
        img = Image.open(path+file)
        new_img = img.resize((500, 500), Image.ANTIALIAS)
        new_img.save('data/landscape-test/'+file)


def check_image_size():
    path = 'data/new/'
    files = os.listdir(path)

    for file in files:
        img = Image.open(path+file)
        if np.asarray(img).shape != (500, 500, 3):
            print(file)


if __name__ == '__main__':
    resize()
