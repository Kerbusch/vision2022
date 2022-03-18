import tensorflow as tf
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Conv2D, MaxPool2D, Dense, Flatten, Dropout
from tensorflow.python.keras.utils.np_utils import to_categorical

import pandas as pd
import numpy as np

digits_train = pd.read_csv("data/train.csv")
train_data_in = digits_train.to_numpy()

# get labels
train_labels = train_data_in[:, 0]  # get first colom from the training data
train_data_without_label = train_data_in[:, 1:]  # remove first colom (labels) from the training data

# make a 3d array (size, 28, 28)
train_data = np.reshape(train_data_without_label, (train_data_without_label.shape[0], 28, 28))

train_data = np.expand_dims(train_data, axis=3)

# variables for model
num_filters = 2
filter_size = (3, 3)
pool_size = (3, 3)

model = Sequential([])

model.add(Conv2D(num_filters, filter_size, padding='same', activation='relu', input_shape=train_data.shape[1:]))