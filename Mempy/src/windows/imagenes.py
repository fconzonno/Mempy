import PySimpleGUI as sg


def build(player_1,board_data,var_x,var_y):
    """
    Construye la ventana del tablero del juego
    """
    layout = [[sg.Button('COMENZAR',key = '-COMENZAR-')],
        [sg.Text(player_1, key='-P1-', text_color='darkblue'),sg.Text('40:00', key="-TIME-", auto_size_text=True)],
        [sg.Text('')]
]

    for y in range(var_y):
        layout += [
            [
                sg.Button(image_filename='signo.png',key = f'cell -{x}-{y}',k = '-TOOGLE-', border_width=0,disabled=True) 
                for x in range(var_x)
            ]
        ]

    board = sg.Window('Nivel 1', keep_on_top=True).Layout(layout)

    return board