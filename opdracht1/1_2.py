import skimage
from skimage import io
from skimage import color

import matplotlib.pyplot as plt

image2 = skimage.io.imread("IMG_20211222_154201.jpg")

image2 = skimage.color.rgb2hsv(image2)

hue_image1 = image2[:, :, 0]

for x in range(image2.shape[0]):
    for y in range(image2.shape[1]):
        if not (0.085 < image2[x][y][0] < 0.119):
            image2[x][y][1] = 0

print("done")
hue_image2 = image2[:, :, 0]
print(hue_image1)

num_bins = 20
#n, bins, patches = plt.hist(hue_image1, num_bins, facecolor='blue', alpha=0.5)
n, bins, patches = plt.hist(hue_image2, num_bins, facecolor='red', alpha=0.5)
plt.show()

#image2 = skimage.color.hsv2rgb(image2)

#viewer = skimage.viewer.ImageViewer(image2)
#viewer.show()
