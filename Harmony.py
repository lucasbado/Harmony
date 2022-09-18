from cProfile import label
from cgitb import text
from importlib.resources import path
from multiprocessing.resource_sharer import stop
import requests
import os
from time import sleep
import speech_recognition as sr
import pyttsx3 
from tkinter import *

robo = pyttsx3.init()

def voz():
    if True:
        os.system("HarmonyVoz.py")

def texto():
    if True:
        os.system("HarmonyChat.py")
        
janela = Tk()  
janela.title("Harmony")
texto_orientacao = Label(janela, text="Olá clique no botao e escolha entre voz e video")
texto_orientacao.grid(column=0, row=0)

consulta = Label(janela, text=" Comandos bot" "\n""\n" " Nivel da agua" "\n""\n"

"Criar rotina" "\n""\n"

"Consultar rotina ""\n" "\n"

"regar" "\n""\n"

"clima" "\n""\n"

"sair")
consulta.grid(column=3, row=1)

botao = Button(janela, text="Voz", command=voz)
botao.grid(column=0, row=2)

botao2 = Button(janela, text="Chat", command=texto)
botao2.grid(column=1, row=2)

janela.mainloop()