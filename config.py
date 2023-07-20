import PySimpleGUI as sg


sg.theme('SystemDefaultForReal')

NUMBER_BUTTONS = 6
BUT_NUMBER_SSS = ['0','0:15','0:30',*[str(i+1) for i in range(NUMBER_BUTTONS)]]
HEADINGS = ["Date","Wasted time"]
DAYS_BEFORE = 7