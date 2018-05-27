import pandas as pd
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation

def build_model():
    model = Sequential()
    model.add(Dense(50, input_dim=16))
    model.add(Activation('relu'))
    model.add(Dense(50))
    model.add(Activation('relu'))
    model.add(Dense(50))
    model.add(Activation('relu'))
    model.add(Dense(50))
    model.add(Activation('relu'))
    model.add(Dense(50))
    model.add(Activation('sigmoid'))
    model.summary()
    return model

def get_data(file_name):
    df = pd.read_csv(file_name)
    df.drop(['ID0', 'ID1', 'ID2', 'ID3', 'ID4'], axis=1, inplace=True)
    return df

def train(model):
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # get X and y here
    model.fit(X, y)
    # perhaps use checkpoints / callbacks

def main():
    df = get_data('../output.csv')
    print df
    # train & save

if __name__ == '__main__':
    main()
