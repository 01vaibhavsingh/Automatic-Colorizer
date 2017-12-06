from skimage.segmentation import slic
from skimage.segmentation import watershed
from skimage.segmentation import quickshift
from skimage.segmentation import felzenszwalb
from skimage.data import imread
from skimage.util import img_as_float
from skimage.io import imsave

from constants import *


def segment_slic(path,  n_segments=N_SEGMENTS):
    img = img_as_float(imread(path))
    segments = slic(img, n_segments=n_segments, compactness=10, sigma=1)
    # segments = watershed(img, markers=250, compactness=0.1)
    # segments = quickshift(img, kernel_size=3, max_dist=6, ratio=0.5)
    # segments = felzenszwalb(img, scale=100, sigma=0.5, min_size=50)
    return img, segments


if __name__ == '__main__':

    img, segments = segment_slic('output/gray.jpg')

    imsave('output/gray-segments.jpg', segments)
