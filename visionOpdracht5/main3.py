import numpy as np
import matplotlib.pyplot as plt
import mnist
import tensorflow.python.data.kernel_tests.test_base

from keras.datasets import cifar10
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from tensorflow.python.keras.utils.np_utils import to_categorical

import tensorflow as tf

from scripts.load_data import load_train, load_test

# Het importeren en bewerken van de data
train_images, train_labels = load_train()
test_images, test_labels = load_test()

# Normalizeren van de images
train_images = (train_images / 255) - 0.5
test_images = (test_images / 255) - 0.5

# Reshapen van de images zodat ze de juiste dimensies hebben
train_images = np.expand_dims(train_images, axis=3)
test_images = np.expand_dims(test_images, axis=3)

print(train_images.shape)


# Onze CNN

# Stap 1: bepaal hoeveel filters je wilt, hoe groot je filter size moet zijn (let op je filter size mag niet te groot zijn vergeleken met je images), en wat je pool size is.
num_filters = 2
filter_size = (28 * 31)
pool_size = 100
# zijn nu random getallen voor de filters

# Stap 2: maak het model.
#    In de array die je aan sequential meegeeft, zet je alle layers die in het model moeten:
#    Conv2D, parameters: num_filters, filter_size, input_shape=(x, y, z)
#    MaxPooling2D, parameters: pool_size=pool_size
#    Flatten,
#    Dense, parameters: aantal outputs, activation='softmax'

model = Sequential([])

#Conv2d
model.add(Conv2D(num_filters, filter_size, padding='same', activation='relu', input_shape=train_images.shape[1:]))
#MaxPooling2d
model.add(MaxPooling2D(pool_size=(3,3)))
#Flatten
model.add(Flatten())
#Dense
model.add(Dense(10, activation='softmax'))

# Stap 3: het compilen van het model.
# model.compile parameters: 'adam', loss='categorial_crossentropy', metrics=['accuracy']
model.compile('adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])


# Stap 4: fit het model.
#    Data om op te trainen: train_images, to_categorial(train_labels)
#    epochs = 3
#    validation_data = test_images, to_categorial(test_labels)
model.fit(train_images, train_labels, epochs=3)#, validation_data= (test_images, to_categorical(test_labels)))