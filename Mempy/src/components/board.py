from itertools import cycle
import PySimpleGUI as sg
import random
import csv
import json

from PySimpleGUI.PySimpleGUI import TIMEOUT_KEY, WINDOW_CLOSED
from src.windows import imagenes
from src.windows import palabras
from src.handlers import board as handler
import time as t
import numpy as np

IMAGENES = ['c:/Users/marcos/Desktop/Mempy/src/Images/Image0.png','c:/Users/marcos/Desktop/Mempy/src/Images/Image0.png',
    'c:/Users/marcos/Desktop/Mempy/src/Images/Image1.png','c:/Users/marcos/Desktop/Mempy/src/Images/Image1.png',
    'c:/Users/marcos/Desktop/Mempy/src/Images/Image2.png','c:/Users/marcos/Desktop/Mempy/src/Images/Image2.png',
    'c:/Users/marcos/Desktop/Mempy/src/Images/Image3.png','c:/Users/marcos/Desktop/Mempy/src/Images/Image3.png',
    'c:/Users/marcos/Desktop/Mempy/src/Images/Image4.png','c:/Users/marcos/Desktop/Mempy/src/Images/Image4.png',
    'c:/Users/marcos/Desktop/Mempy/src/Images/Image5.png','c:/Users/marcos/Desktop/Mempy/src/Images/Image5.png',
    'c:/Users/marcos/Desktop/Mempy/src/Images/Image6.png','c:/Users/marcos/Desktop/Mempy/src/Images/Image6.png',
    'c:/Users/marcos/Desktop/Mempy/src/Images/Image7.png','c:/Users/marcos/Desktop/Mempy/src/Images/Image7.png',
    'c:/Users/marcos/Desktop/Mempy/src/Images/Image8.png','c:/Users/marcos/Desktop/Mempy/src/Images/Image8.png',
    'c:/Users/marcos/Desktop/Mempy/src/Images/Image9.png','c:/Users/marcos/Desktop/Mempy/src/Images/Image9.png' ]

def cargarTablero(usuario,board_data, x, y):                     ################### COPIAR Y PEGAR
    '''Esta funcion carga el tablero empezado del usuario'''
    try: 
        lista = usuario['Tablero']
        contador = 0
        for i in range(0,x):
            for j in range(0,y):
                board_data[i][j].estado = lista[contador][0] ##como hago el set?
                board_data[i][j].imagen_carta = lista[contador][1]  ##como hago el set?

                print(board_data[i][j].estado)
                print(board_data[i][j].imagen_carta)   
                contador += 1
    except Exception as ex:
        sg.popup('Ha ocurrido un error al cargar el tablero')
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        sg.popup(message) 



def guardarTablero(board_data, x, y):             ################### COPIAR Y PEGAR
    '''Esta funcion guarda el tablero actual'''
    try: 
        lista = []
        for i in range(0,x):
            data = board_data[i].tolist()
            for j in range(0,y):
                tupla= [data[j].estado, data[j].imagen_carta]
                lista.append(tupla)
                print(tupla)
        return lista
    except Exception as ex:
        sg.popup('Ha ocurrido un error al guardar la jugada')
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        sg.popup(message) 


def agregarTablero(usuario, board_data, x, y):                  ################### COPIAR Y PEGAR
    '''agrega el tablero como parte de los datos del usuario'''
    try:
        with open ('usuarios.json', 'r', encoding = 'utf8') as file:      ## actualiza el csv de usuarios
            listaUsuarios = json.load(file)
            usuario['Tablero'] = guardarTablero(board_data, x, y)    
            user = list(filter(lambda a: a['Nombre'] == usuario['Nombre'], listaUsuarios))  #BUSCAR USUARIO ESPECIFICO CON FILTER Y CAMBIARLO EN LA LISTA DE USUARIOS 
            usuarioDesactualizado = user[0]
        with open ('usuarios.json', 'w', encoding = 'utf8') as file: 
            listaUsuarios.remove(usuarioDesactualizado)
            listaUsuarios.append(usuario)
            json.dump(listaUsuarios, file, indent = 4, ensure_ascii = 4)

            with open('usuarios.csv','w') as csv_file:
                write = csv.writer(csv_file)
                write.writerow(listaUsuarios[0].keys())       
                for x in listaUsuarios:
                    write.writerow(x.values())
    except:
        sg.popup('Hubo un error al actualizar el csv de los usuarios')


    try:
        with open ('jugadas.csv', 'w') as csv_file:        ## creo un csv sólo con las jugadas del usuario actual
            write = csv.writer(csv_file)
            write.writerow(usuario.keys())
            write.writerow(usuario.values())
    except:
        sg.popup('Ocurrió un error al crear el csv con las jugadas del usuario actual')

class Carta:
    def __init__(self, imagen):
        self._state = False
        self._imagen = imagen
    
    def get_state(self):
        return self._state
    
    def set_state(self,state):
        self._state = state

    def get_imagen (self):
        return(self._imagen)	
		
    def set_imagen (self, imagen):
	    self._imagen = imagen

    estado = property(get_state,set_state)
    imagen_carta = property(get_imagen,set_imagen)



def start(usuario):
    print(usuario['Dificultad'])
    if usuario['Imagenes'] == True:
        window = loopimagenes(usuario)
        window.close()
    # else:
    #     window = looppalabras() 
    #     window.close()

def desbloquearBotones(window,board_data,x,y):
    for i in range (y):
        for j in range (x):
            if board_data[j][i].estado == False:
                window[f'cell -{j}-{i}'].update(disabled=False)



def loopimagenes(usuario):
    if usuario['Dificultad'] == 'Nivel 1':
        x = 3
        y = 4
        cartas = 12
        tiempo = 39
    
    elif usuario['Dificultad'] == 'Nivel 2':
        x = 4
        y = 4
        cartas = 16
        tiempo = 49
    else:
        x = 4
        y = 5
        cartas = 20
        tiempo = 59
    carta = Carta('')   

    board = []
    
    if (usuario['Tablero'] != [] ):       ## si el tablero esta vacio entonces nunca jugo, por lo tanto, paso
        for i in range(cartas):
            carta = Carta('')
            board.append(carta)
        board_data = np.array(board).reshape(x,y)
        cargarTablero(usuario,board_data, x, y)
        partida_nueva = False
    else:
        for i in range(cartas):
            carta = Carta(IMAGENES[i])
            board.append(carta)
        random.shuffle(board)
        board_data= np.array(board).reshape(x,y)  

    window = imagenes.build(usuario['Nombre'],board_data,x,y)

    n = None
    jugadas = cycle([1,2])
    jugada = next(jugadas)
    while True:
        event, _values = window.read(timeout=n)

        if event == WINDOW_CLOSED:
            break
        if event == '-COMENZAR-':
            desbloquearBotones(window,board_data,x,y)
            start_time = t.time()
            n = 1
            window[event].update(disabled=True)
            estado = ''
            evento = 'inicioPartida'
            handler.guardarArchivoJugadasTotales(usuario, estado, evento)
        if event.startswith('cell'):
            if jugada == 1:
                handler.play(window,event,board_data,usuario)
                jugada = next(jugadas)
                event1 = event
                agregarTablero(usuario, board_data, x, y)
            else: 
                handler.play(window,event,board_data,usuario)
                window.refresh()
                t.sleep(0.5)
                handler.check_image(window,event1,event,board_data,usuario) 
                jugada = next(jugadas)
                agregarTablero(usuario, board_data, x, y)
            if handler.check_win(board_data,x,y,usuario) == True:
                estado = 'ok'
                evento= 'fin'
                usuario['Tablero'] = []
                usuario['TiempoJugado'] = current_time % 60
                agregarTablero(usuario, board_data, x, y)
                handler.guardarArchivoJugadasTotales(usuario, estado, evento)
                sg.Popup('Ganaste',keep_on_top=True)
                window.close()
                break
        
        current_time = t.time() - start_time
        if round(tiempo - current_time % 60) == 0:
            estado = 'Error'
            evento= 'fin'
            usuario['Tablero'] = []
            usuario['TiempoJugado'] = current_time % 60
            handler.guardarArchivoJugadasTotales(usuario, estado, evento)
            sg.Popup('Perdiste wey',keep_on_top=True)
            window.close()
            break

            
        window['-TIME-'].update(f"00:{round(tiempo - current_time % 60):02d}") 


# start()

