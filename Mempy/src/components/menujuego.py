import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED
from src.windows import menujuego
from src.components import board




def start(player):
    """
    Lanza la ejecución de la ventana del menú
    """
    window = loop(player)
    window.close()


def loop(player):
    """
    Loop de la ventana de menú que capta los eventos al apretar las opciones
    """
    window = menujuego.build(player)

    while True:
        event, values = window.read()

        if event == 'None' or event == '-volver-' or event == None or WINDOW_CLOSED:
            break         
        if values['-niveles-'] == '':
            sg.Popup('No se ingresó ningún nivel, volvé a ingresar los datos')
        elif values['-dificultad-'] == '':
            sg.Popup('No se ingresó ninguna dificultad, volvé a ingresar los datos')
        else:
            board.start(player,values['-niveles-'],values['-dificultad-'])



    return window