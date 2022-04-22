from re import M
import turtle  
import numpy as np
import random


nn = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'Barrel', 'Flage', 'PoffHon', 'Silence', 'Slap', 'Slide']

n = [random.choice(nn) for x in range(100)]

def draw(notes: list):
    
    window = turtle.Screen()
    window.bgcolor('black')
    window.title('GuitarGrapher')
    window.setup(700, 700)
    window.colormode(255)
    
    t = turtle.Turtle()
    
    note_keys = {
        'A': [(0, 204, 0), 50, t.forward, 40],
        'B': [(0, 0, 255), 120, t.right, 45],
        'C': [(255, 0, 0), 75, t.backward, 80],
        'D': [(255, 255, 0), 100, t.left, 35],
        'E': [(255, 153, 0), 45, t.forward, 20],
        'F': [(102, 153, 0), 65, t.backward, 70],
        'G': [(255, 102, 153), 80, t.right, 10],
        'Barrel': [(153, 51, 51), 110, t.left, 50],
        'Flage' : [(255, 255, 255), 200, t.forward, 100],
        'PoffHon' : [(102, 0, 102), 130, t.backward, 40],
        'Silence' : [(255, 102, 102), 60, t.circle, 20],
        'Slap' : [(102, 0, 255), 70, t.right, 30],
        'Slide' : [(51, 102, 153), 150, t.forward, 65]
    }

    t.pensize(20)
    for note in notes:
        t.color(note_keys[note][0])
        t.speed(note_keys[note][1])
        note_keys[note][2](note_keys[note][3])
    
    window.exitonclick()
        
draw(n)
    
    