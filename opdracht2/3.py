import matplotlib.pyplot as plt
from skimage import data, filters, feature
from skimage.viewer import ImageViewer
import scipy
from scipy import ndimage

image = data.camera()

edge1 = feature.canny(image, sigma=2.3, low_threshold=0.80, high_threshold=0.85, use_quantiles=True)
edge2 = feature.canny(image, sigma=2)

fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(8, 3))

ax[0].imshow(image, cmap='gray')
ax[0].set_title('standard', fontsize=20)

ax[1].imshow(edge1, cmap='gray')
ax[1].set_title('canny 2.1 met threshold', fontsize=20)

ax[2].imshow(edge2, cmap='gray')
ax[2].set_title('canny 2', fontsize=20)

for a in ax:
    a.axis('off')

fig.tight_layout()
plt.show()
