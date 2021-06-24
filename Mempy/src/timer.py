import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('00:00', key="-TIME-", auto_size_text=True)],
          #   [sg.Text('Enter something on Row 2'), sg.InputText()],
          [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Window Title', layout, size=(800, 800))
# Event Loop to process "events" and get the "values" of the inputs
tiempo = 0
while True:
    print(tiempo)
    event, values = window.read(timeout=1000)
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    tiempo += 1
    window.FindElement("-TIME-").Update("{}:{}".format(str(tiempo // 60), str(tiempo)))


window.close()