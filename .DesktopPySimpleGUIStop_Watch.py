# SimplePythonGUI-Examples - 1
import PySimpleGUI as sg
from time import sleep
mins, secs = 0,0
layout = [[sg.Text('Time remaining: ',size=(20,2),justification='center')],
          [sg.Text(text='{:02d}:{:02d}'.format(mins,secs), size=(20,2), key='-DISPLAY-', justification='center')],
           [sg.Button(button_text='Start'),sg.Button(button_text='Stop'),sg.Button(button_text='Reset'),sg.Button(button_text='Quit')]]
window = sg.Window('Stopwatch', layout)



#event loop
timeSpent = 0
startStop = False
while True:
    event, values = window.read(timeout=10)

    #allow user to close program
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    #allow user to start the stopwatch
    if event == 'Start':
        startStop = True
    if event == 'Stop':
        startStop = False
    if event == 'Reset':
        timeSpent = 0 #shouldn't need to update min or secs because these will be updated before they are used below
        mins, secs = 0,0
        window['-DISPLAY-'].update('{:02d}:{:02d}'.format(mins,secs))
        startStop = False
        

    # stopwatch runs here
    if startStop == True:
        mins, secs = divmod(timeSpent,60)
        window['-DISPLAY-'].update('{:02d}:{:02d}'.format(mins,secs))
        #print(mins, secs, timeSpent, startStop)
        timeSpent += 1
        sleep(1)
    
window.close()
