import pyaudio
import numpy as np
import time
from tqdm import tqdm

from tensorflow import keras
from abc import ABC
import librosa as lb
import numpy as np

#----------------------------------------------------------Perhaps this class does not belong here, but I did not figure out where to put it
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
                        12: 'Slide',
                        13: 'Silence'}




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



#-----------------------------------------------------------------------And these guys are clearly in the right place.
def feature_exctractor(auddata: np.array) -> np.array:
    """Function to convert the audio data into an array for the model to work with

    Args:
        auddata (np.array): Data array received from librosa.load(file)

    Returns:
        np.array: weighted array mel spectrogram
    """
    
    data = lb.feature.mfcc(auddata, n_mfcc=2048)
    data = np.mean(data, axis=1)

    return np.log(data ** 2)



def listen(chunk=4096, rate=44100, device=1, timer=10):
    
    """Function of recognition of notes from the input data from the microphone
    
    Args:
        chunk [int]: Input chunk size
        rate [int]: Sampling frequency
        device [int]: Microphone ID
        timer [int]: Function running time

    Returns:
        predicted [list]: list of predicted note values
    """
    
    # Microphone and ML model initializing
    p = pyaudio.PyAudio()
    model = AModel()
    
    stream = p.open(format=pyaudio.paInt32,
                    channels=2,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk,
                    input_device_index=device)
    
    predicted = []
    
    t = timer * 6
    
    # Delay to prepare
    for i in range(5, 0, -1):
        print(f'Recording will start in {i} sec ')
        time.sleep(1)
    print('RECORDING...')
    
    # Main loop
    while t:
        
        time.sleep(0.4)
        indata = np.fromstring(stream.read(chunk), dtype=np.int32)
        
        fftData = abs(np.fft.rfft(indata)) ** 2
        
        res = model.dpredict(fftData[1:])
        predicted.append(res)
        print(res)
        t -= 1
        
    return predicted 