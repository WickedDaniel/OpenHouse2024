
from msvcrt import getch
from Modules.Chatbot import Run
import os

# Create Program Manipulation Methods
def ExitProgram():
    exit()

def ClearOutput():
    os.system("cls")

def GetInputKey():
    return  ord(getch())


# Program Information
Settings = {
    "CurrentSelection": type[int],
    "CurrentMenu": callable
}

ChBindCode = {
    #49: Keyboard.1 -> Ingreso
    #51: Keyboard.3 -> Salida
    49: Run,
    51: ExitProgram
}

def CoreLoop():
    # Clean up and get input
    ClearOutput()
    print("Bienvenido usuario! A continuación te muestro el menu de opciones.")
    print("[1] Interactuar con el ChatBot")
    print("[2] Salir del programa")

    while True:
        Settings["CurrentSelection"] = GetInputKey()
        if not Settings["CurrentSelection"] in ChBindCode: continue
        break

    Settings["CurrentMenu"] = ChBindCode[Settings["CurrentSelection"]]
    # Cut down the name
    Menu = Settings["CurrentMenu"]
    if not hasattr(Menu, '__call__') : return

    # Run respective menu
    Menu()

def Run():
    while True:
        CoreLoop()