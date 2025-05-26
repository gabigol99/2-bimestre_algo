compras = ["pão", "café", "leite"]
print(compras)

#pode remoover pelo nome do produto ou pelo indice
#compras.remove("pão")
compras.remove(compras[0])
print(compras)

#append acrescenta um item no final da lista, só pode adicionar um por vez 
compras.append("açucar")
print(compras)

compras_ordenada = sorted(compras)
print(compras_ordenada)

#o nome item é um identificador dos itens dentro da lista, esses itens podem receber qualquer tipo de nome
for panela in compras_ordenada:
    print("-", panela)