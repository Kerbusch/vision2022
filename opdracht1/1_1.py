import skimage
from skimage import io
from skimage import color

image2 = skimage.io.imread("IMG_20211222_154201.jpg")

image2 = skimage.color.rgb2hsv(image2)

for x in range(image2.shape[0]):
    for y in range(image2.shape[1]):
        if not (0.09 < image2[x][y][0] < 0.11):
            image2[x][y][1] = 0

image2 = skimage.color.hsv2rgb(image2)

viewer = skimage.viewer.ImageViewer(image2)
viewer.show()
