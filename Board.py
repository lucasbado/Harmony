#by Jp - 24.02.2022
import pyfirmata #Importamos a biblioteca PyFirmata que realiza a comunicação entre Python e Arduino
import time #Importamos também a biblioteca padrão Time, com o objetivo de setar as pausas e marcações temporais entre as piscadas.
pin = 13 #Definimos para o Python que nosso pino é o 13.
port = 'COM3' #Configuramos a porta como a porta COM4. Esta configuração deve ser alterada caso sua placa não se configure nesta porta.
board = pyfirmata.Arduino(port) #Criamos a variável board que realizará os comandos a partir daqui
 
numeroBlink = input('Insira o número de vezes que o LED deve piscar:  ') #Temos um input, que pede ao usuário para inserir um número de piscadas para o LED realizar
print("Piscando " + numeroBlink + " vezes.") #Com este comando opcional, imprimimos na tela quantas vezes o led irá piscar.
 
for x in range(int(numeroBlink)):#A cada elemento no escopo da variável numeroBlink, realizar os seguintes comandos:
      board.digital[13].write(1)#Utilizamos a variável board e seu método .Digital para dizer ao pino 13 que ele deve acender
      time.sleep(1)#Colocamos uma pausa de 0.01 segundos
      board.digital[13].write(0)#Utilizamos a variável board e seu método .Digital para dizer ao pino 13 que ele deve apagar
      time.sleep(1)#Colocamos uma pausa de 0.01 segundos