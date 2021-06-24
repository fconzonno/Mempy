from threading import Timer
from tkinter.constants import DISABLED
from typing import Text
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import B, R, WINDOW_CLOSED
import random 
import numpy as np
import time


IMAGENES = ['c:/Users/marcos/Desktop/Juego/src/Images/Image0.png','c:/Users/marcos/Desktop/Juego/src/Images/Image0.png',
    'c:/Users/marcos/Desktop/Juego/src/Images/Image1.png','c:/Users/marcos/Desktop/Juego/src/Images/Image1.png',
    'c:/Users/marcos/Desktop/Juego/src/Images/Image2.png','c:/Users/marcos/Desktop/Juego/src/Images/Image2.png',
    'c:/Users/marcos/Desktop/Juego/src/Images/Image3.png','c:/Users/marcos/Desktop/Juego/src/Images/Image3.png',
    'c:/Users/marcos/Desktop/Juego/src/Images/Image4.png','c:/Users/marcos/Desktop/Juego/src/Images/Image4.png',
    'c:/Users/marcos/Desktop/Juego/src/Images/Image5.png','c:/Users/marcos/Desktop/Juego/src/Images/Image5.png',
    'c:/Users/marcos/Desktop/Juego/src/Images/Image6.png','c:/Users/marcos/Desktop/Juego/src/Images/Image6.png',
    'c:/Users/marcos/Desktop/Juego/src/Images/Image7.png','c:/Users/marcos/Desktop/Juego/src/Images/Image7.png',
    'c:/Users/marcos/Desktop/Juego/src/Images/Image8.png','c:/Users/marcos/Desktop/Juego/src/Images/Image8.png',
    'c:/Users/marcos/Desktop/Juego/src/Images/Image9.png','c:/Users/marcos/Desktop/Juego/src/Images/Image9.png' ]

cd

    #return all(matriz[x][y].state == True for x in range(3) and y in range(4))

class Carta:
    def __init__(self, imagen):
        self.state = False
        self.imagen = imagen

carta = Carta('')      
board = []
for i in range(12):
    carta = Carta(IMAGENES[i])
    board.append(carta)
    

random.shuffle(board)

matriz= np.array(board).reshape(3,4)

layout = [
        [sg.Text('Jugador 1: ', key='-P1-', text_color='darkblue'),sg.Text('00:00', key="-TIME-", auto_size_text=True)],
        [sg.Text('')]
]

for y in range(4):
        layout += [
            [
                sg.Button(image_filename='signo.png',key = f'cell -{x}-{y}',k = '-TOOGLE-', border_width=0,) 
                for x in range(3)
             ]
        ]

window = sg.Window('Prueba',layout,keep_on_top=True)
while True:
    event,_value = window.read()
    if event == WINDOW_CLOSED:
        break
    if event.startswith('cell'):
        prefix, x, y = event.split("-")
        if(matriz[int(x)][int(y)].state == False):
            window[event].update(image_filename=matriz[int(x)][int(y)].imagen, disabled = True )
        else:
            window[event].update(image_filename='signo.png')
    event2,_value2 = window.read()
    if event2 == WINDOW_CLOSED:
        break
    if event2.startswith('cell'):
        prefix2, i, j = event2.split("-")
        if(matriz[int(i)][int(j)].state == False):
            window[event2].update(image_filename=matriz[int(i)][int(j)].imagen )
        
        else:
            window[event2].update(image_filename='signo.png')
    if matriz[int(x)][int(y)].imagen == matriz[int(i)][int(j)].imagen:
        window[event2].update(disabled = True)
        matriz[int(x)][int(y)].state = True
        matriz[int(i)][int(j)].state = True
        win = check_win(matriz)
        
            


    else:
        sg.PopupAnnoying(auto_close = True, auto_close_duration=0.50,keep_on_top=False,modal=False)
        window[event].update(image_filename='signo.png', disabled = False)
        window[event2].update(image_filename='signo.png')
    
        
    