lista = []
sair = False

while sair == não:
    print("deseja adicionar um item na lista?")
    resposta = input("sim ou nao")
    if resposta == "sim":
        item = input("digite o nome do item a ser adicionado")
        lista.append(item)
        print("lista atual: ", lista)
    else:
        print("deseja excluir um item da lista?")
        resposta2 = input("sim ou nao:")
        if resposta2 == "sim":
            item = input("digite o nome do item a ser removido")
            if item in lista:
                lista.remove(item)
                print("lista atual: ", lista)
            else:
                print("item nao encontrado")
        else:
            print("deseja finalizar?")
            sair = input("sim ou nao")
print("programa finalizado. lista final: ", lista)
            
