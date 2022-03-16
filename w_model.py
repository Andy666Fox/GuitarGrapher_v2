from tensorflow import keras
from abc import ABC
import librosa as lb
import numpy as np
from torch import classes


class Model(ABC):

    def __init__(self):
        self.model = keras.models.load_model('./model')
        self.classes = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'Barrel': 8, 'Flage': 9, 'PoffHon': 10, 'Slap': 11, 'Slide': 12}

    def feature_exctractor(self, auddata):
        data = lb.feature.mfcc(auddata, n_mfcc=128)
        data= np.mean(data, axis=1)

        return data

    def predict(self, aud) -> str:
        to_predict = feature_exctractor(aud)
        classid = np.argmax(self.model.predict(to_predict)[0])

        return classes[classid]