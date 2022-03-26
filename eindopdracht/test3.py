import tensorflow as tf
import numpy as np


(train_images, train_labels), (_, _) = tf.keras.datasets.mnist.load_data()

num = 4

x = list()

for i in range(train_labels.shape[0]):
    if train_labels[i] == num:
        x.append(i)

train_images = train_images[x]
train_labels = train_labels[x]
