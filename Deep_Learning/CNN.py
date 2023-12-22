'''
A Convolutional Neural Network (ConvNet/CNN) is a Deep Learning algorithm that can take in 
an input image, assign importance (learnable weights and biases) to various aspects/objects in 
the image, and be able to differentiate one from the other.

In a CNN, we first have:
Convolutional and Pooling Layers:

'''



import numpy as np
import keras
from keras.datasets import mnist
from keras.models import Model
from keras.layers import Dense, Input
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten
from keras import backend as k

(x_train, y_train), (x_test, y_test) = mnist.load_data()

img_rows, img_cols = 28, 28

if k.image_data_format() == 'channels_first':
    