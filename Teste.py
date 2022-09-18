from cProfile import label
import requests
import os
from time import sleep
import speech_recognition as sr
import pyttsx3 
from tkinter import *


 

def teste():
    print("teste")
    print("Como posso ajudar?")
    texto_bot["text"] = "teste"



janela = Tk()  
janela.title("Harmony")
texto_orientacao = Label(janela, text="Olá clique no botao e escolha entre voz e video")
texto_orientacao.grid(column=0, row=0)

nilo = Entry(janela, text="Digite o nome da planta")
nilo.grid(column=0, row=4)

texto_bot = Label(janela, text="")
texto_bot.grid(column=0, row=3)

botao = Button(janela, text="print", command=teste)
botao.grid(column=0, row=1)





janela.mainloop()