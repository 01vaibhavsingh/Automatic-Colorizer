from PIL import Image
import numpy as np
import os


def convert():
    img = Image.open('output/color.JPG').convert('L')
    img.save('output/gray.JPG')


def check():
    path = 'data/landscape/'
    files = os.listdir(path)

    for file in files:
        img = Image.open(path+file)
        if np.asarray(img).ndim < 3:
            print(file)


if __name__ == '__main__':
    check()