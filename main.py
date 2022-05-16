from funcs import *
import numpy as np
from art import text2art

import warnings

warnings.filterwarnings("ignore")
warnings.simplefilter(action="ignore", category=FutureWarning)

def run():
    logo = text2art('GUITAR GRAPHER')
    print(logo)
    ch = input('[?] Start recording? (y/n): ')
    if ch.lower() == 'y':
        timer = input('[?] Recording time (sec): ')
        aarr = listen(timer=int(timer))
        
    elif ch.lower() == 'n':
        print('Cancellation. Have a nice day!')
        
    else:
        print(f'Incorrect input: {timer}')
    
if __name__ == '__main__':
    run()
