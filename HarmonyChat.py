from distutils.cmd import Command
import os
from time import sleep
from Api import Weather
from datetime import datetime
import json
from pathlib import Path

dict1 = {}

print("Como posso ajudar?")

while True:
    resposta = input("")
    resposta = resposta.lower()

    if "nível da água" in resposta:
        print("digite o nivel da agua")
        niv = int(input("Digite o nível da água: "))
        if niv > 50:
            print("O nível da água está em " + (niv) + " centímetros")
            print("O nível da água está normal")
        else:
            print("O nível da água está em " + (niv) + " centímetros")
            print("O nível da água está baixo")
            print("Deseja ligar a bomba?")
            resposta = input("")
            if "sim" in resposta:
                print("Bomba ligada")
                print("a bomba irá ligar por 5 segundos")
                sleep(5)
                while sleep == True :
                    print(".")
                print("Bomba desligada")
                break
            else:
                print("Okay, não ligo a bomba")
                break

    if "criar rotina" in resposta:
       

        print("Digite o nome da planta")
        nome = input("")
        Path('./Rotinas').mkdir(parents=True, exist_ok=True)
        arquivo = open("./Rotinas/" + nome + ".json", "w")
        arquivo.write("Nome: " + nome + "\n")

        print("Digite o horário da rotina")
        horario = input("")
        arquivo.write( "Horario: " + horario + "\n")
        
        print("Digite os dias da rotina")
        dia = input("")
        arquivo.write( "Dia: " + dia + "\n")

        print("Digite o que a rotina irá fazer")
        acao = input("")
        arquivo.write("Acao: " + acao + "\n")
        
        
        with open("./Rotinas/" + nome + ".json", "r" ) as arquivo:
            for linha in arquivo:
                command, desciption = linha.strip().split(None, 1)
                dict1[command] = desciption.strip()

        arquivo=open("./Rotinas/" + nome + ".json", "w")
        json.dump(dict1, arquivo, indent=1, sort_keys=False)
        arquivo.close()


        print("Rotina criada com sucesso")
        data = json.load("./Rotinas/" + nome + ".json")
        print(data)
        break

    if "consultar rotina" in resposta:
        print("Digite o nome da rotina")
        nome = input("")
        arquivo = open("./Rotinas/" + nome + ".json", "r")
        data = json.load(arquivo)
        print(data)
        break

    if "regar" in resposta:
        print("Ligando bomba...")
        print("Regando...")
        print("Bomba desligada")
        break

    if "clima" in resposta:
        print("Qual cidade?")
        clima = input("")
        print ("aguarde...")
        city = clima
        print(Weather.get_weather(city))
        break
        




    if "sair" in resposta:
        print("Até mais!")
        break
    
    else:
        print("Não entendi, tente novamente")
        continue
    

