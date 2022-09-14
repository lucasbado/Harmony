from ast import Break
from datetime import datetime
import speech_recognition as sr
import pyttsx3
import pyautogui as ag
from Api import Weather
from pathlib import Path
import json

dict1 = {}
recon = sr.Recognizer()
resposta = ""
hora = (str(datetime.today().hour) + ":" + str(datetime.today().minute))
data = (str(datetime.today().day) + "/" + str(datetime.today().month) + "/" + str(datetime.today().year))
diasDaSemana = ("segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo")


parar = False

with sr.Microphone(1) as source:
    while not "não" in resposta:
        robo = pyttsx3.init()
        robo.say(" Posso ajudar em alguma coisa?")
        print("Posso ajudar em alguma coisa?")
        voices = robo.getProperty('voices')
        robo.setProperty("brazil", voices[2].id)
        robo.setProperty('rate',180)
        robo.setProperty('volume', 1)
        robo.runAndWait()

        
    
        while True:

            audio = recon.listen(source)
            recon.adjust_for_ambient_noise(source, duration=0.2)
            res = recon.recognize_google(audio, language='pt-BR')
            resposta = res.lower()
            print("Texto reconhecido: ", resposta)
            
            if "nível da água" in resposta:
                print("digite o nivel da agua")
                robo.say("digite o nivel da agua")
                robo.runAndWait()
                niv = int(input("Digite o nível da água: "))
               

                if niv > 50:
                    robo = pyttsx3.init()
                    robo.say("O nível da água está em " + str(niv) + " centímetros")
                    print("O nível da água está em " + str(niv) + " centímetros")
                    voices = robo.getProperty('voices')
                    robo.setProperty("brazil", voices[2].id)
                    robo.setProperty('rate',180)
                    robo.setProperty('volume', 1)
                    robo.runAndWait()
                    robo = pyttsx3.init()
                    robo.say("O nível da água está normal")
                    print("O nível da água está normal")
                    voices = robo.getProperty('voices')
                    robo.runAndWait()
                    break
                else:
                    robo = pyttsx3.init()
                    robo.say("O nível da água está em " + str(niv) + " centímetros")
                    print("O nível da água está em " + str(niv) + " centímetros")
                    voices = robo.getProperty('voices')
                    robo.setProperty("brazil", voices[2].id)
                    robo.setProperty('rate',180)
                    robo.setProperty('volume', 1)
                    robo.runAndWait()
                    robo = pyttsx3.init()
                    robo.say("O nível da água está baixo")
                    print("O nível da água está baixo")
                    voices = robo.getProperty('voices')
                    robo.runAndWait()
                    
                    robo.say("Deseja ligar a bomba?")
                    print("Deseja ligar a bomba?")
                    voices = robo.getProperty('voices')
                    robo.runAndWait()
                    audio = recon.listen(source)
                    recon.adjust_for_ambient_noise(source)
                    res = recon.recognize_google(audio, language='pt-BR')
                   
                    resposta = res.lower()
                    print("Texto reconhecido: ", resposta)
                    if "sim" in resposta:
                        robo = pyttsx3.init()
                        robo.say("Ligando a bomba")
                        print("Ligando a bomba")
                        voices = robo.getProperty('voices')
                        robo.setProperty("brazil", voices[2].id)
                        robo.setProperty('rate',180)
                        robo.setProperty('volume', 1)
                        robo.runAndWait()
                        break
                    else:
                        robo = pyttsx3.init()
                        robo.say("Okay, não irei ligar a bomba")
                        print("Okay, não irei ligar a bomba")
                        voices = robo.getProperty('voices')
                        robo.setProperty("brazil", voices[2].id)
                        robo.setProperty('rate',180)
                        robo.setProperty('volume', 1)
                        robo.runAndWait()
                        break
                       
               
                        

                
           
            #wether with a API from openweathermap.org
            if "clima" in resposta:
                robo.say("Qual a cidade?")
                print("Qual a cidade?")
                robo.runAndWait()
                audio = recon.listen(source)
                recon.adjust_for_ambient_noise(source)
                clima = recon.recognize_google(audio, language='pt-BR')
               
                city = clima.lower()
                print (Weather.get_weather(city))
                robo.say(Weather.get_weather(city))
                robo.runAndWait()
                break

           
       
            if "criar rotina" in resposta:
                robo.say("Qual o nome da planta?")
                print("Qual o nome da rotina?")
                robo.runAndWait()
                audio = recon.listen(source)
                recon.adjust_for_ambient_noise(source)
                nome = recon.recognize_google(audio, language='pt-BR')
               
                Path('./Rotinas').mkdir(parents=True, exist_ok=True)
                arquivo = open("./Rotinas/" + nome + ".json", "w")
                arquivo.write("Nome: " + nome + "\n")
                
                # robo.say("Para quando deseja criar a rotina?")
                # print("Para quando deseja criar a rotina?")
                # robo.runAndWait()
                # audio = recon.listen(source)
                recon.adjust_for_ambient_noise(source)
                # res = recon.recognize_google(audio, language='pt-BR')
                #
                # resposta = res.lower()
                # print("Texto reconhecido: ", resposta)
                
                robo.say("Qual o horário da rotina?")
                print("Qual o horário da rotina?")
                robo.runAndWait()
                audio = recon.listen(source)
                recon.adjust_for_ambient_noise(source)
                res = recon.recognize_google(audio, language='pt-BR')
               
                horario = res.lower()
                print("Texto reconhecido: ", horario)
                arquivo.write("Horario: " + horario + "\n")
              
                robo.say("Qual o dia da rotina?")
                print("Qual o dia da rotina?")
                robo.runAndWait()
                audio = recon.listen(source)
                recon.adjust_for_ambient_noise(source)
                res = recon.recognize_google(audio, language='pt-BR')
               
                dia = res.lower()
                print("Texto reconhecido: ", dia)
                arquivo.write("Dia: " + dia + "\n")

                robo.say("O que a rotina irá fazer?")
                print("O que a rotina irá fazer?")
                robo.runAndWait()
                audio = recon.listen(source)
                recon.adjust_for_ambient_noise(source)
                res = recon.recognize_google(audio, language='pt-BR')
               
                acao = res.lower()
                print("Texto reconhecido: ", acao)
                arquivo.write("Acao: " + acao + "\n")

            
                with open("./Rotinas/" + nome + ".json", "r") as arquivo:
                    for linha in arquivo:
                        command, desciption = linha.strip().split(None, 1)
                        dict1[command] = desciption.strip()
                
                arquivo=open("./Rotinas/" + nome + ".json", "w")
                json.dump(dict1, arquivo, indent=1, sort_keys=False)
                arquivo.close()

                robo.say("Arquivo criado com sucesso")
                print("Arquivo criado com sucesso")
                robo.runAndWait()
                data = json.load(open("./Rotinas/" + nome + ".json"))
                json.dumps(data, indent=1)
                print(data)
                robo.say(data)
                
                break

            if "ler rotina" in resposta:
                robo.say("Qual o nome da rotina?")
                print("Qual o nome da rotina?")
                robo.runAndWait()
                audio = recon.listen(source)
                recon.adjust_for_ambient_noise(source)
                nome = recon.recognize_google(audio, language='pt-BR')
                arquivo = open("./Rotinas/" + nome + ".json", "r")
                data = json.load(open("./Rotinas/" + nome + ".json"))
                json.dumps(data, indent=1)
                print(data)
                robo.say(data)
                robo.runAndWait()
                break
            

            if "saindo" in resposta:
                robo.say("OK! Até mais tarde senhor!")
                robo.runAndWait()
                parar = True
                break

            else:
                robo.say("Desculpa nao entendi! Poderia repetir?")
                robo.runAndWait()
                print("Desculpa nao entendi! Poderia repetir?")
                continue

