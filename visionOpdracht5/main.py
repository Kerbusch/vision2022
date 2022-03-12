import mnist
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple
from scipy.signal import convolve2d

from scripts.load_data import load_train


def convolve(image, filt):
    """
    Task: Bouw een functie die over een foto heen glijdt en de dot product op ieder punt berekend
    en de som van daarvan terugzet in een output array.

    image: een 28x32 numpy array
    filt: een 3x3 array
    """

    output_array = np.zeros((image.shape[0] - 2, image.shape[1] - 2))
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            x = 0
            for n in range(len(filt)):
                for m in range(len(filt[0])):
                    x += image[i+n-1][j+m-1] * filt[n][m]
            output_array[i-1][j-1] = x

    return output_array


X_train, y_train = load_train()

# TODO selecteer een cijfer uit de training set
image_to_filter = X_train[2]
plt.imshow(image_to_filter)
plt.show()
print(image_to_filter.shape)

# the filter to be used for convolution
u_filter = [[0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]]

# print image and the output after convolution
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

axs[0].imshow(image_to_filter)
axs[0].set_title("image before filter")

x_ = convolve(image_to_filter, u_filter)

#TODO zet de met behulp van de eerder geschreven functie de afbeelding om tot de activatie map
axs[1].imshow(x_)
axs[1].set_title("image after filter")

plt.show()
