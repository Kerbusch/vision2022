import matplotlib.pyplot as plt
from skimage import data, filters, feature
from skimage.viewer import ImageViewer
import scipy
from scipy import ndimage

image = data.camera()

mask1 = [[1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9]]
newimage = scipy.ndimage.convolve(image, mask1)
newimage = scipy.ndimage.convolve(newimage, mask1)

edge1 = feature.canny(newimage, sigma=1.5)
edge2 = feature.canny(newimage, sigma=2)

fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(8, 3))

ax[0].imshow(newimage, cmap='gray')
ax[0].set_title('standard', fontsize=20)

ax[1].imshow(edge1, cmap='gray')
ax[1].set_title('canny 1.5', fontsize=20)

ax[2].imshow(edge2, cmap='gray')
ax[2].set_title('canny 2', fontsize=20)

for a in ax:
    a.axis('off')

fig.tight_layout()
plt.show()
