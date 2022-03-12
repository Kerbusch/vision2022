import mnist
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple
from scipy.signal import convolve2d

from scripts.load_data import load_train

X_train, y_train = load_train()

#---------------------------------
def max_pooling(image, n):
    """
    Task: Bouw een functie die over een afbeelding heen glijdt en per regio van n breed en n hoog
    het maximale element eruit haalt en deze in een output array zet.

    image: een 28x32 numpy array
    n: de grootte van de pool size
    """

    # stap 1
    # vraag de shape op van de image en bouw alvast de output array
    # hint: check hoe vaak de 'pool size' erin past

    horizontal = int(28 / n)
    vertical = int(32 / n)
    outputArray = np.zeros((horizontal, vertical))

    # stap 2
    # loop over de hoogte en breedte van de output
    # hint: Wanneer we over de output itereren zal een index out of bounds kunnen voorkomen

    for x in range(horizontal):
        for y in range(vertical):
            outputArray[x][y] = np.maximum(image[x*2][y*2], np.maximum(image[x*2+1][y*2], np.maximum(image[x*2][y*2+1], image[x*2+1][y*2+1])))

    # stap 3
    # selecteer de regio waar de filter in moet zoeken naar het maximale element
    # gebruik slices en een np functie

    # stap 4
    # return de output array

#---------------------------------

image_to_pool = X_train[2]  # afbeelding van de nummer 7
print(image_to_pool.shape)
plt.imshow(image_to_pool)
plt.show()

# TODO voer de pooling functie uit over de afbeelding met een n = 2
image_after_pool = max_pooling(image_to_pool, 2)

# print image and the output after convolution
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

axs[0].imshow(image_to_pool)
axs[0].set_title("image before pooling\nshape: {0}".format(image_to_pool.shape))

axs[1].imshow(image_after_pool)
axs[1].set_title("image after pooling\nshape: {0}".format(image_after_pool.shape))

plt.show()