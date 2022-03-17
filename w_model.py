from tensorflow import keras
from abc import ABC
import librosa as lb
import numpy as np
from torch import classes


def feature_exctractor(auddata):
        data = lb.feature.mfcc(auddata, n_mfcc=128)
        data = np.mean(data, axis=1)

        return data


class AModel(ABC):

    def __init__(self):
        self.model = keras.models.load_model('./model')
        self.classes = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'Barrel', 9: 'Flage', 10: 'PoffHon', 11: 'Slap', 12: 'Slide'}


    def dpredict(self, aud) -> str:

        if np.std(aud) < 1.4:
            print('Silence')
            return 0
        else:
        
            to_predict = np.array([feature_exctractor(aud)])
            classid = np.argmax(self.model.predict(to_predict)[0])

            return self.classes[classid]