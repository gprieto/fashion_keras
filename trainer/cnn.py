import keras
import h5py

from datetime import datetime # for filename conventions
import numpy as np
import pandas as pd

import argparse

from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, Conv2D, MaxPool2D, MaxPooling2D, Flatten
import keras.metrics as metrics

from tensorflow.python.lib.io import file_io # for better file I/O
import sys

# Create a function to allow for different training data and other options
def train_model(train_file='data/fashion/fashion-mnist_train',
				job_dir='./tmp/fashion', **args):
	# set the logging path for ML Engine logging to Storage bucket
	logs_path = job_dir + '/logs/' + datetime.now().isoformat()
	print('Using logs_path located at {}'.format(logs_path))

	Labels = ["T-shirt/top",
	"Trouser",
	"Pullover",
	"Dress",
	"Coat",
	"Sandal",
	"Shirt",
	"Sneaker",
	"Bag",
	"Ankle boot"]

	f = file_io.FileIO(train_file, mode='r')

	data_train = pd.read_csv(f,engine='python')			

	img_rows, img_cols = 28, 28
	input_shape = (img_rows, img_cols, 1)

	X_train = np.array(data_train.iloc[:, 1:])
	y_train_ohe = to_categorical(np.array(data_train.iloc[:, 0]))

	X_train = X_train.reshape(len(y_train_ohe), img_rows * img_cols)
	X_train = X_train.astype('float32')
	X_train /= 255


	N = X_train.shape[0]
	batch_size = 32

	n_batch = int(N/batch_size)

	dropout_rate=0.1

	model = Sequential()

	model.add(Conv2D(16, (5, 5), activation='relu', input_shape=input_shape))
	model.add(MaxPooling2D(pool_size=(2, 2)))

	model.add(Conv2D(16, (5, 5), activation='relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))

	model.add(Flatten())
	model.add(Dense(200, activation='relu'))
	model.add(Dropout(dropout_rate))
	model.add(Dense(10, activation='softmax'))


	def top3_acc(ytrue, ypred):
	    return metrics.top_k_categorical_accuracy(ytrue, ypred, k=3)

	# Change decay for better results

	# lr: 1e-3, decay: 0

	model.compile(loss=keras.losses.categorical_crossentropy,
	              optimizer=keras.optimizers.SGD(lr=0.001, decay=0., nesterov=False), 
	             metrics=[metrics.categorical_accuracy, top3_acc])

	history = model.fit(X_train.reshape(-1, 28, 28, 1), y_train_ohe, epochs=5, batch_size=32,verbose=2)

	score = model.evaluate(X_train, y_train_ohe, verbose=0)
    print('Train loss:', score[0])
    print('Train accuracy:', score[1])

		# Save the model locally
	model.save('model_cnn.h5')

if __name__ == '__main__':
	# Parse the input arguments for common Cloud ML Engine options
	parser = argparse.ArgumentParser()
	parser.add_argument(
	  '--train-file',
	  help='Cloud Storage bucket or local path to training data')
	parser.add_argument(
	  '--job-dir',
	  help='Cloud storage bucket to export the model and store temp files')
	args = parser.parse_args()
	arguments = args.__dict__
	train_model(**arguments)