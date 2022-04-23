import matplotlib.pyplot as plt 
import numpy as np 


def draw(aarr: list):
    notes = []
    for note in aarr:
        notes.append(note[0])
        plt.plot(note[1])
        
    plt.legend(list(set(notes)))
    plt.show()
    
    

    
    
    