import os
from time import sleep
from Api import Weather
import os
from datetime import datetime


print("Como posso ajudar?")

while not "sair" in resposta:
    resposta = input("")

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
       

        print("Digite o nome da rotina")
        nome = input("")
        arquivo = open(nome + ".txt", "w")

        print("Digite o horário da rotina")
        horario = input("")
        arquivo.write("Horário: " + horario + "\n")
        
        print("Digite os dias da rotina")
        dia = input("")
        arquivo.write("Dia: " + dia + "\n")

        print("Digite o que a rotina irá fazer")
        acao = input("")
        arquivo.write("Ação:" + acao + "\n")

        arquivo.close()
        print("Rotina criada com sucesso")
        print (arquivo.read())
        break
    if "executar rotina" in resposta:
        print("Digite o nome da rotina")
        nome = input("")
        arquivo = open(nome + ".txt", "r")
        print(arquivo.read())
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
    

