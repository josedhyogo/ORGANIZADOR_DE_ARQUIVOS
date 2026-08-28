import PySimpleGUI as sg

layout = [[sg.Text('This is our persistent window')],
          [sg.Button('1'), sg.Button('2'), sg.Button('Exit')]]

window = sg.Window('Title', layout)

while True:         # The Event Looop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == '1':
        sg.popup('You clicked 1')
    elif event == '2':
        sg.popup('You clicked 2')

window.close()