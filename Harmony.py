
import os
from time import sleep
import speech_recognition as sr
import pyttsx3  

robo = pyttsx3.init()



while True:
    print("Olá eu sou a harmony. Escreva 'voz' para falar comigo ou 'texto' para escrever comigo ou 'sair' para sair")
    robo.say("Olá eu sou a harmony. Escreva 'voz' para falar comigo ou 'texto' para escrever comigo ou 'sair' para sair")
    robo.runAndWait()
    resposta = input("Escreva 'voz' ou 'texto' para escolher o modo ou 'sair' para sair: ")
    print("voce escolheu: " + resposta)
    if resposta == "voz":
        os.system("HarmonyVoz.py")
    elif resposta == "texto":
        os.system("HarmonyChat.py")
    elif resposta == "sair":
        print("Até mais!")
    else:
        print("Opção inválida, tente novamente!")
        continue
