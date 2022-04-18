# Imports
from tensorflow import keras
from abc import ABC
import librosa as lb
import numpy as np


# Function from 'model.ipynb' file
def feature_exctractor(auddata: np.array) -> np.array:
    """Function to convert the audio data into an array for the model to work with

    Args:
        auddata (np.array): Data array received from librosa.load(file)

    Returns:
        np.array: weighted array mel spectrogram
    """
    
    data = lb.feature.mfcc(auddata, n_mfcc=2048)
    data = np.mean(data, axis=1)

    return data


# Main Audio Model class
class AModel(ABC):

    def __init__(self):
        self.model = keras.models.load_model('./model')
        self.classes = {1: 'A', 
                        2: 'B', 
                        3: 'C', 
                        4: 'D', 
                        5: 'E', 
                        6: 'F', 
                        7: 'G', 
                        8: 'Barrel', 
                        9: 'Flage', 
                        10: 'PoffHon', 
                        11: 'Slap', 
                        12: 'Slide'}




    def dpredict(self, aud: np.array) -> str:
        
        """Wrapper for convenient work with model predictions
        
        Args:
            aud (np.array): Data received from the feature_extractor() function

        Returns:
            dict[key]: Model predicted class
        """

        to_predict = np.array([feature_exctractor(aud)])
        classid = np.argmax(self.model.predict(to_predict)[0])

        return self.classes[classid]