#import tensorflow as tf
#from tensorflow.keras import layers

import pandas as pd
import numpy as np

digits_train = pd.read_csv("data/train.csv")
print(digits_train.shape)
train_data = digits_train.to_numpy()

#get labels
train_labels = train_data[:,0] #get first colom from the training data
train_data = train_data[:,1:] #remove first colom (labels) from the training data

#make 2d 28x28 array
np.reshape

print(train_labels)
