from ast import Break
from datetime import datetime
import speech_recognition as sr
import pyttsx3
import pyautogui as ag
from Api import Weather

recon = sr.Recognizer()
resposta = ""
hora = (str(datetime.today().hour) + ":" + str(datetime.today().minute))
data = (str(datetime.today().day) + "/" + str(datetime.today().month) + "/" + str(datetime.today().year))
diasDaSemana = ("segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo")


parar = False

with sr.Microphone(2) as source:
    while not "não" in resposta:
        
        robo = pyttsx3.init()
        robo.say("Posso ajudar em alguma coisa?")
        print("Posso ajudar em alguma coisa?")
        voices = robo.getProperty('voices')
        robo.setProperty("brazil", voices[2].id)
        robo.setProperty('rate',180)
        robo.setProperty('volume', 1)
        robo.runAndWait()

        
    
        while True:

            audio = recon.listen(source)
            res = recon.recognize_google(audio, language='pt-BR')
            recon.adjust_for_ambient_noise(source, duration=4)
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
                    res = recon.recognize_google(audio, language='pt-BR')
                    recon.adjust_for_ambient_noise(source, duration=4)
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

            

            if "saindo" in resposta:
                robo.say("OK! Até mais tarde senhor!")
                robo.runAndWait()
                parar = True
                break

            else:
                robo.say("Okay, muito obrigado! Até mais tarde senhor!")
                robo.runAndWait()
                print("Okay, muito obrigado! Até mais tarde senhor!")
                Break

