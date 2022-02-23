import skimage.transform
from skimage import data, filters
from skimage.viewer import ImageViewer
import numpy as np
import scipy
from scipy import ndimage

image = data.camera()

image = skimage.img_as_float(image)  # is dit nodig?

angle = 90
rotate_matrix2 = np.array([[np.cos(angle), np.arcsin(angle), 0],
                           [np.sin(angle), np.cos(angle), 0],
                           [0, 0, 1]])
# werkt niet bij arcsin. krijg een output van "nan"

#image_rotated = skimage.transform.warp(image, skimage.transform.AffineTransform(matrix=rotate_matrix))
#viewer = ImageViewer(image_rotated)
#viewer.show()

transformation = (40, 80)
trans_matrix = np.array([[1, 0, transformation[0]],
                         [0, 1, transformation[1]],
                         [0, 0, 1]])

image_trans = skimage.transform.warp(image, trans_matrix)
viewer = ImageViewer(image_trans)
#viewer.show()

shear = 7.0
shear_matrix = np.array([[1, shear, 0],
                         [0, 1, 0],
                         [0, 0, 1]])

image_stretch = skimage.transform.warp(image, shear_matrix)
viewer = ImageViewer(image_stretch)
viewer.show()