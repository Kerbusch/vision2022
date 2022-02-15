from skimage import data, filters
from skimage.viewer import ImageViewer
import scipy
from scipy import ndimage

image = data.camera()
viewer = ImageViewer(image)
viewer.show()

mask1 = [[1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9]]
newimage = scipy.ndimage.convolve(image, mask1)
newimage = scipy.ndimage.convolve(newimage, mask1)
viewer = ImageViewer(newimage)
viewer.show()

mask1 = [[1 / 7, 1 / 7, 1 / 7], [1 / 7, 1 / 7, 1 / 7], [1 / 7, 1 / 7, 1 / 7]]
newimage = scipy.ndimage.convolve(image, mask1)
newimage = scipy.ndimage.convolve(newimage, mask1)
viewer = ImageViewer(newimage)
viewer.show()


mask1 = [[1 / 5, 1 / 5, 1 / 5], [1 / 5, 1 / 5, 1 / 5], [1 / 5, 1 / 5, 1 / 5]]
newimage = scipy.ndimage.convolve(image, mask1)
newimage = scipy.ndimage.convolve(newimage, mask1)
viewer = ImageViewer(newimage)
viewer.show()

mask1 = [[1 / 3, 1 / 3, 1 / 3], [1 / 3, 1 / 3, 1 / 3], [1 / 3, 1 / 3, 1 / 3]]
newimage = scipy.ndimage.convolve(image, mask1)
newimage = scipy.ndimage.convolve(newimage, mask1)
viewer = ImageViewer(newimage)
viewer.show()
