#uma empresa de logistica gerencia pacotes enviados e recebidos em seu centro de distribuicao. Cada pacote tem um codigo de rastreamento e um status entrega. O sistema da empresa armazena esses informaçãoes em tuplas imutaveis para evitar alterações indevidas nos registros.
#pacotes =( ("ABC123", "Enviado"), ("XYZ789", "Recebido"), ("DEF456", "Entransito"), ("JKL321", "Enviado"), ("MNO654", "Recebido"), ("PQR987", "Entransito"), ("STU741", Enviado),)
#A empresa precisa implementar um programa que: 1. Conte quantos pacotes estão em cada status: "Enviado", "Recebido", "Entransito". 2. Liste apenas o codigo dos pacotes com status "Em transito" 3. Use uma função que recebe um codigo de rastreamento e retorne o status do pacote, ou uma mensagem informando que o pacote nao não está cadastrado. 4. Ordene os pacotes pelo codigo de rastreamento e exiba a tupla ordenada. Desenvolva um programa em Python que execute essas operações e exiba os resultados, explicando o metodo de implementação.

pacotes = (("ABC123", "Enviado"), ("XYZ789", "Recebido"), ("DEF456", "Em_transito"), ("JKL321", "Enviado"), ("MNO654", "Recebido"), ("PQR987", "Em_transito"), ("STU741", "Enviado"))

enviados = 0
recebidos = 0
em_transito = 0

rastreamento = input("insira o codigo de rastreamento")

for codigo, status in pacotes:
    if status == "Enviado":
        enviados += 1
    elif status == "Recebido":
        recebidos += 1
    elif status == "Em_transito":
        em_transito += 1

print(f"Enviados: {enviados}")
print(f"Recebidos: {recebidos}")
print(f"Em transito: {em_transito}")

for codigo, status in pacotes:
    if status == "Em_transito":
        print(codigo)





