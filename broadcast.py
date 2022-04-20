# Imports
import pyaudio
import numpy as np
from IPython.display import clear_output
from w_model import AModel, feature_exctractor
import time
from tqdm import tqdm


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
    time.sleep(2)
    print('Registration will start in 5...')
    time.sleep(1)
    print('Registration will start in 4..')
    time.sleep(1)
    print('Registration will start in 3.')
    time.sleep(1)
    print('Registration will start in 2')
    time.sleep(1)
    print('Registration will start in 1.')
    time.sleep(1)
    print('RECORDING...')
    
    # Main loop
    while tqdm(t):
        
        time.sleep(0.4)
        indata = np.fromstring(stream.read(chunk), dtype=np.int32)
        
        fftData = abs(np.fft.rfft(indata)) ** 2
        
        res = model.dpredict(fftData[1:])
        predicted.append(res)
        print(res)
        t -= 1
        
    return predicted  

ppd = listen(timer=7)
print(ppd)
        
    
    