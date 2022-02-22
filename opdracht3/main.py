import skimage.transform
from skimage import data, filters
from skimage.viewer import ImageViewer
import numpy as np
import scipy
from scipy import ndimage

image = data.camera()

image = skimage.transform.rotate(image, 90)
viewer = ImageViewer(image)
viewer.show()

image = skimage.transform.
viewer = ImageViewer(image)
viewer.show()

image = skimage.transform.AffineTransform()
viewer = ImageViewer(image)
viewer.show()
