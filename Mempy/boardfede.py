from json.encoder import JSONEncoder
import PySimpleGUI as sg
import random
import json
import csv

from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED
from src.windows import imagenes
from src.windows import palabras
from src.handlers import board as handler
import time
import numpy as np

IMAGENES = ['c:/Users/fconz/Desktop/Mempy/Mempy/src/Images/Image0.png','c:/Users/fconz/Desktop/Mempy/Mempy/src/Images/Image0.png',
    'c:/Users/fconz/Desktop/Mempy/Mempy/src/Images/Image1.png','c:/Users/fconz/Desktop/Mempy/Mempy/src/Images/Image1.png',
    'c:/Users/fconz/Desktop/Mempy/Mempy/src/Images/Image2.png','c:/Users/fconz/Desktop/Mempy/Mempy/src/Images/Image2.png',
    'c:/Users/fconz/Desktop/Mempy/Mempy/src/Images/Image3.png','c:/Users/fconz/Desktop/Mempy/Mempy/src/Images/Image3.png',
    'c:/Users/fconz/Desktop/Mempy/Mempy/src/Images/Image4.png','c:/Users/fconz/Desktop/Mempy/Mempy/src/Images/Image4.png',
    'c:/Users/fconz/Desktop/Mempy/Mempy/src/Images/Image5.png','c:/Users/fconz/Desktop/Mempy/Mempy/src/Images/Image5.png',
    'c:/Users/fconz/Desktop/Mempy/Mempy/src/Images/Image6.png','c:/Users/fconz/Desktop/Mempy/Mempy/src/Images/Image6.png',
    'c:/Users/fconz/Desktop/Mempy/Mempy/src/Images/Image7.png','c:/Users/fconz/Desktop/Mempy/Mempy/src/Images/Image7.png',
    'c:/Users/fconz/Desktop/Mempy/Mempy/src/Images/Image8.png','c:/Users/fconz/Desktop/Mempy/Mempy/src/Images/Image8.png',
    'c:/Users/fconz/Desktop/Mempy/Mempy/src/Images/Image9.png','c:/Users/fconz/Desktop/Mempy/Mempy/src/Images/Image9.png' ]
# class NumpyEncoder(json.JSONEncoder):
#     """ Special json encoder for numpy types """
#     def default(self, obj):
#         if isinstance(obj, np.integer):
#             return int(obj)
#         elif isinstance(obj, np.floating):
#             return float(obj)
#         elif isinstance(obj, np.ndarray):
#             return obj.tolist()
#         return json.JSONEncoder.default(self, obj)

# class Object:
#     def toJSON(self):
#         return json.dumps(self, default=lambda o: o.__dict__, 
#             sort_keys=True, indent=4)

# def guardarJugada(board_data):
    
#     ''' Guarda cada jugada que realiza el usuario'''
#     try:
#         with open('jugada.json', 'w',encoding = 'utf8') as file:
#             dumped = json.dumps(board_data, cls=NumpyEncoder)
#             print(dumped)
#     #         jugada = JugadasEncode().encode(dumped)
#     #         print(jugada)
#     #         json.dump(jugada, file, indent = 4, ensure_ascii = 4)
#     #         sg.popup('Se cargó la jugada correctamente', auto_close_duration= 2, auto_close=True)
#     except Exception as ex:
#         sg.popup('Ha ocurrido un error al guardar la jugada')
#         template = "An exception of type {0} occurred. Arguments:\n{1!r}"
#         message = template.format(type(ex).__name__, ex.args)
#         sg.popup(message) 

# def crearCsv():
#     '''Esta función crea el archivo csv que guardará las jugadas'''
#     try:
#         with open ('jugadas.csv', 'w') as csv_file:
#             write = csv.writer(csv_file)
    # try:
    #     with open ('usuarios.json', 'r', encoding = 'utf8') as file:
    #         listaUsuarios = json.load(file)
    #         with open('usuarios.csv','w') as csv_file:
    #             write = csv.writer(csv_file)
    #             write.writerow(listaUsuarios[0].keys())       #guarda primero el encabezado
    #             for x in listaUsuarios:
    #                 write.writerow(x.values())
    #         sg.popup('El archivo con los usuarios se creó correctamente y se llama: "usuarios.csv" ', auto_close_duration= 3, auto_close=True )
    # except FileNotFoundError:
    #     sg.popup('No se encontró el archivo, por lo tanto, es el primer usuario en ingresar y No está registrado, lo rediccionaremos a la pantalla de registro')
    #     registrar()
    #     return




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

# class JugadasEncode(JSONEncoder):
#     def default (self, o):
#         return o.__dict__
# def cargarTablero (usuario):
#     '''Esta funcion carga el tablero ya empezado por el usuario'''
#     try:
#         with open ('usuarios.json', 'r', encoding = 'utf8') as file:     
#             listaUsuarios = json.load(file)
#     except:
#         sg.popup('Ocurrio un error al cargar el tablero')





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
                tupla = (data[j].estado, data[j].imagen_carta)
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



def start(usuario):
    print(usuario['Dificultad'])
    if usuario['Imagenes'] == True:
        window = loopimagenes(usuario)
        window.close()
    # else:
    #     window = looppalabras() 
    #     window.close()



def loopimagenes(usuario):
    if usuario['Dificultad'] == 'Nivel 1':
        x = 3
        y = 4
        cartas = 12
    
    elif usuario['Dificultad'] == 'Nivel 2':
        x = 4
        y = 4
        cartas = 16
    else:
        x = 4
        y = 5
        cartas = 20
    carta = Carta('')   

    board = []

    # if (usuario['Tablero'] != [] ):       ## si el tablero esta vacio entonces nunca jugo, por lo tanto, paso
    #     cargarTablero(usuario,board_data, x, y)
    
    for i in range(cartas):
        carta = Carta(IMAGENES[i])
        board.append(carta)
    
    random.shuffle(board)
    
    board_data= np.array(board).reshape(x,y)    



    window = imagenes.build(usuario['Nombre'],board_data,x,y)


    while True:
        event, _values = window.read()

        if event == WINDOW_CLOSED:
            agregarTablero(usuario, board_data, x, y)  ################### COPIAR Y PEGAR
            break

        if event.startswith('cell'):
            handler.play(window,event,board_data)
            agregarTablero(usuario, board_data, x, y) ################### COPIAR Y PEGAR

        
        event2,_values2 = window.read()

        if event2 == sg.WINDOW_CLOSED:
            agregarTablero(usuario, board_data, x, y) ################### COPIAR Y PEGAR
            break
        if event2.startswith('cell'):
            handler.play(window,event2,board_data)
            handler.check_image(window,event,event2,board_data) == True
            agregarTablero(usuario, board_data, x, y) ################### COPIAR Y PEGAR

        if handler.check_win(board_data,x,y) == True:
            usuario['Tablero'] = []                    ################### COPIAR Y PEGAR
            sg.Popup('Ganaste',keep_on_top=True)
            break
        
            


# start()

