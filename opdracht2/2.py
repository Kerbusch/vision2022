from skimage import data, filters
from skimage.viewer import ImageViewer
import scipy
from scipy import ndimage

image = data.camera()
viewer = ImageViewer(image)
viewer.show()

new_image_sobel = filters.sobel(image)
new_image_roberts = filters.roberts(image)
new_image_scharr = filters.scharr(image)

viewer = ImageViewer(new_image_sobel)
viewer.show()

viewer = ImageViewer(new_image_roberts)
viewer.show()

viewer = ImageViewer(new_image_scharr)
viewer.show()

# Het valt op dat alle output afbeeldingen haast hetzelfde zijn. Ze hebben ook allemaal hetzelfde doel.

