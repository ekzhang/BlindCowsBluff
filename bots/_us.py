import pandas as pd
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.callbacks import ModelCheckpoint, CSVLogger

def build_model():
    model = Sequential()
    model.add(Dense(50, input_dim=23))
    model.add(Activation('relu'))
    model.add(Dense(50))
    model.add(Activation('relu'))
    model.add(Dense(50))
    model.add(Activation('relu'))
    model.add(Dense(50))
    model.add(Activation('relu'))
    model.add(Dense(1))
    model.add(Activation('sigmoid'))
    model.summary()
    return model

def fix_cow(row):
    cow = int(row[0])
    row = list(row[1:])
    return pd.Series(row[cow*4+1:] + row[:cow*4])

def get_data(file_name, labels_name):
    X = pd.read_csv(file_name)
    X.drop(['ID0', 'ID1', 'ID2', 'ID3', 'ID4', 'ID5', 'Action', 'Amount'], axis=1, inplace=True)
    X = X.apply(fix_cow, axis=1)
    y = pd.read_csv(labels_name)
    return X, y

def train(model, X, y):
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(X, y, callbacks=[CSVLogger('_us_training.log'), ModelCheckpoint('_us_model.{epoch:02d}.hdf5')])
    # perhaps use checkpoints / callbacks

def main():
    X, y = get_data('../output.csv', '../output-labels.csv')
    model = build_model()
    train(model, X, y)



if __name__ == '__main__':
    main()
