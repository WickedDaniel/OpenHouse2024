from Modules.Training import Respuesta
from msvcrt import getch
import os

Active = False
global Username
def ExitProgram():
    exit()
def GetInputKey():
    return  ord(getch())
def ClearOutput():
    os.system("cls")
def Deactivate():
    global Active
    Active = False
def Activate():
    global Active
    Active = True

ChBindCode = {
    #49: Keyboard.1 -> Ingreso
    #51: Keyboard.3 -> Salida
    27: Deactivate,
    13: Activate
}

def CoreLoop():
    Response, typ = Respuesta(input('Usuario: '))
    print('Chatbot sobre la especialidad: {}'.format(Response))
    print("\nPresione [Enter] si desea realizar otra pregunta, si no, presione [ESC]")

    while True:
        InputKey = GetInputKey()
        if not InputKey in ChBindCode: continue
        if not hasattr(ChBindCode[InputKey], '__call__') : continue
        ChBindCode[InputKey]()
        break

    ClearOutput()

def Run():
    ClearOutput()
    print("Chatbot sobre la especialidad: Hola, es un gusto conocerte!")
    print("Como chatbot tengo mis limitaciones, aún así intentare comprender el contexto de la mejor manera!")
    print("Puedes empezar preguntandome algo como 'Que voy a hacer en la especialidad?'")

    Activate()
    while Active:
        CoreLoop()