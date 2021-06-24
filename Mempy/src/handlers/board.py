import PySimpleGUI as sg
import csv
from src import components

def guardarArchivoJugadasTotales(usuario, estado, evento):
    
    try:
        usuario['NombreEvento'] = evento
        usuario['Estado'] = estado    
        with open ('jugadasTotales.csv', 'x' , encoding = 'utf8') as csv_file:
            write = csv.writer(csv_file)
            write.writerow(usuario.keys()) 
            write.writerow(usuario.values())
    except:
        with open ('jugadasTotales.csv', 'a', encoding = 'utf8') as csv_file:
            write = csv.writer(csv_file)             
            write.writerow(usuario.values())





def play(window, event, board_data, usuario):
    """
    Ejecuta una jugada sobre el tablero para un jugador:
    - Actualiza el tablero visual
    - Agrega el valor en board_data
    - Chequea si ganó '''"""
    prefix, x, y = event.split("-")
    window[event].update(image_filename=board_data[int(x)][int(y)].imagen_carta, disabled = True )

    return board_data


def check_image(window,event,event2,board_data, usuario):
    """
    Chequea si las imágenes coinciden y si todas las imágenes estan dadas vuelta
    """
    prefix, x, y = event.split("-")
    prefix2, i, j = event2.split("-")
    if board_data[int(x)][int(y)].imagen_carta == board_data[int(i)][int(j)].imagen_carta:
        window[event2].update(disabled = True)
        board_data[int(x)][int(y)].estado = True
        board_data[int(i)][int(j)].estado = True
        estado = 'Ok'
        
    else:
        sg.PopupAnnoying(auto_close = True, auto_close_duration=0.50,keep_on_top=False,modal=False)
        window[event].update(image_filename='signo.png', disabled = False)
        window[event2].update(image_filename='signo.png', disabled = False)
        estado = 'Error'
    evento = 'Intento'
    guardarArchivoJugadasTotales(usuario,estado, evento)
    
        
    return board_data


def check_win(matriz,x,y,usuario):
    """
    Chequea la si una jugada ganadora esta completa
    """
    res = []
    for i in range (x):
        for j in range (y):
            res.append(matriz[i][j].estado == True)
    return all(res)
