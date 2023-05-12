listapronta = ["leite", "pão"]
lista = []
certeza = "não"
nome_definido = "nao"
encerrar = "cu"
mostrar = "aa"
adicionado = False
a = True
while a == True:
    print("seja bem vindo a sua lista de comprars, oque vc deseja? ")
    print("1: para ver sua antiga lista \n2: para criar novalista")
    cacacaca = str(input("==>  "))
    if cacacaca == "2":
        while nome_definido != "sim":
            print("Qual nome vc quer a sua lista?")
            nome = str(input("==>  "))
            print(f"vc tem certeza que o nome desejada é {nome}? ")
            nome_definido = str(input("==>  "))

        while encerrar != "sim" or encerrar != "s":
            print(f"voce deseja adicionar algo a {nome}? atualmente ela contem {len(lista)}")
            adicionar = str(input("==> "))
            if adicionar == "sim" or encerrar == "s":
                if adicionado == False:
                    print("oq voce deseja adicionar? ")
                    pedido = (str(input("==>  ")))
                    if pedido == "nada":
                        break
                    else:
                        lista.append(pedido)
                        print("item adicionado")
                    adicionado = True
                    continue

                elif adicionado == True:
                    print("oq mais voce deseja adicionar? ")
                    pedido = (str(input("==>  ")))
                    if pedido == "nada":
                        break
                    else:
                        lista.append(pedido)
                        print("item adicionado")

                print("deseja visualizar a lista?")
                mostrar = str(input("==>"))
                if mostrar == "sim":
                    print(lista)

    elif cacacaca == "1":
        print("esta opção esta em construção")
        continue
        cacacaca = 0

    else:
        print("comando desconhecido")
        continue
        cacacaca = 0