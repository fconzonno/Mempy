import matplotlib
import pandas as pd
import csv
import PySimpleGUI as sg
from matplotlib import pyplot as plt    



sg.theme('BrightColors')

data_set = pd.read_csv('usuarios.csv', encoding='utf-8',error_bad_lines=False)


grupo = data_set[['Nombre','TiempoJugado']]

top3 =(sorted(grupo, key = lambda x:x[1])) 


print(grupo)