#maquina de lavar louça 
#vidro (120 segundos, 100 graus celcius)
#plastico (60 segundos, 21 graus celcius)
#metal (120 segundos, 30 graus celcius)

import time

ligado = False
tempo = 0
potencia = 0

def ligar(novo_tempo, nova_potencia):
    global ligado, tempo, potencia
    if not ligado:
        ligado = True
        tempo = novo_tempo
        potencia = nova_potencia
        print(f"maquina ligada por {tempo} segundos na potencia {potencia}")
        iniciar_cronometro(tempo)
        desligar()
    else:
        print("A maquina ja esta ligada")

def desligar():
    global ligado, tempo, potencia
    if ligado:
        ligado = False
        print("Maquina desligada")
    else:
        print("A maquina ja esta desligada")

def status():
    if ligado:
        print(f"tempo: {tempo} segundos \n potencia: {potencia}")
    else:
        print(f"desligado")

def iniciar_cronometro(segundos):
    while segundos > 0:
        print(f"tempo restante: {segundos} segundos", end="\r")
        time.sleep(1)
        segundos -= 1
        print("\n tempo esgotado")

def vidro():
    ligar(120, 100)

def plastico():
    ligar(60, 21)

def metal():    
    ligar(120, 30)

escolha = input("escolha uma das opcoes: \n1 vidro \n2 plastico \n3 metal")

if escolha == "1":
    vidro()
elif escolha == "2":
    plastico()
elif escolha == "3":
    metal()
else:
    print("opcao invalida")
