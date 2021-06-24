import PySimpleGUI as sg
from src.components import board

dificultad = ['Facil', 'Normal', 'Dificil']
niveles = ['Nivel 1','Nivel 2', 'Nivel 3']
def build(player):
    layout = [
        [sg.Text("¡Hola "+player+"!")]
        [sg.Text("Seleccione el nivel que desea jugar")]
        [sg.InputCombo(niveles,auto_size_text= True, key = '-nivel-')]
        [sg.InputCombo(dificultad, auto_size_text= True,key = '-dificultad-')]
        [sg.Ok(), sg.Button('Volver',key='-volver-')]
    ]
    board = sg.Window('Preferencias',layout)
    board.open()
    return board

build(lol)
 

