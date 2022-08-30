from asyncore import write
from datetime import datetime
import os
import speech_recognition as sr
import webbrowser
import pyttsx3
import pickle
import os.path
import time
import pyautogui as ag

from Api import Weather

recon = sr.Recognizer()
resposta = ""
ardu = ("robô")
hora = (str(datetime.today().hour) + ":" + str(datetime.today().minute))
data = (str(datetime.today().day) + "/" + str(datetime.today().month) + "/" + str(datetime.today().year))
diasDaSemana = ("segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo")







parar = False

with sr.Microphone(1) as source:
    while not parar:
        
        robo = pyttsx3.init()
        robo.say("Oi, eu sou a Harmony, a sua auxiliar de plantação. O que gostaria?")
        print("Oi, eu sou a Harmony, a sua auxiliar de plantação. O que gostaria?")
        voices = robo.getProperty('voices')
        robo.setProperty("brazil", voices[2].id)
        robo.setProperty('rate', 140)
        robo.setProperty('volume', 1)
        robo.runAndWait()   
    
        while True:

            audio = recon.listen(source)
            res = recon.recognize_google(audio, language='pt-BR')
            recon.adjust_for_ambient_noise(source, duration=4)
            resposta = res.lower()
            print("Texto reconhecido: ", resposta)
            
            if "nível da agua" in resposta:
                robo.say("O nivel da agua é de 0,5 litros")
                print("O nivel da agua é de 0,5 litros")
                robo.runAndWait()
                break
           
            #wether with a API from openweathermap.org
            if "clima" in resposta:
                robo.say("Qual a cidade?")
                print("Qual a cidade?")
                robo.runAndWait()
                audio = recon.listen(source)
                clima = recon.recognize_google(audio, language='pt-BR')
                recon.adjust_for_ambient_noise(source, duration=4)
                city = clima.lower()
                print (Weather.get_weather(city))
                robo.say(Weather.get_weather(city))
                robo.runAndWait()
                break

           
       
            if "criar rotina" in resposta:
                robo.say("Para quando deseja criar a rotina?")
                print("Para quando deseja criar a rotina?")
                robo.runAndWait()
                audio = recon.listen(source)
                res = recon.recognize_google(audio, language='pt-BR')
                recon.adjust_for_ambient_noise(source, duration=4)
                resposta = res.lower()
                print("Texto reconhecido: ", resposta)
                
                if diasDaSemana or "Hoje" or "amanhã" in resposta:
                    robo.say("Criando rotina para " + resposta)
                    print("Criando rotina para " + resposta)
                    arquivo = open(resposta + ".txt", "w")
                    robo.runAndWait()

                    robo.say("Qual horario deseja criar a rotina?")
                    print("Qual horario deseja criar a rotina?")
                    robo.runAndWait()
                    
                    audio = recon.listen(source)
                    res = recon.recognize_google(audio, language='pt-BR')
                    recon.adjust_for_ambient_noise(source, duration=4)
                    resposta = res.lower()
                    print("Texto reconhecido: ", resposta)
                    arquivo.write(resposta + "\n")

                    robo.say("Qual nome da planta que deseja criar a rotina?")
                    print("Qual nome da planta que deseja criar a rotina?")
                    robo.runAndWait()

                    audio = recon.listen(source)
                    res = recon.recognize_google(audio, language='pt-BR')
                    recon.adjust_for_ambient_noise(source, duration=4)
                    resposta = res.lower()
                    print("Texto reconhecido: ", resposta)
                    arquivo.write(resposta + "\n")

                
                    robo.say("Qual a quantidade de dias que deseja criar a rotina?")
                    print("Qual a quantidade de dias que deseja criar a rotina?")
                    robo.runAndWait()

                    audio = recon.listen(source)
                    res = recon.recognize_google(audio, language='pt-BR')
                    recon.adjust_for_ambient_noise(source,)
                    resposta = res.lower()
                    print("Texto reconhecido: ", resposta)
                    arquivo.write(resposta + "\n")
                    arquivo.close()
                    robo.say("Arquivo criado com sucesso")
                    print("Arquivo criado com sucesso")
                    robo.runAndWait()
                    break

         

            elif "saindo" in resposta:
                robo.say("OK! Até mais tarde senhor!")
                robo.runAndWait()
                parar = True
                break

            # If the user doesn't say anything (silence) keep recording audio to send it later
            elif resposta == None:
                robo.say("O que você disse?")
                robo.runAndWait()
                continue

            