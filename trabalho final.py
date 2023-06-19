import sys
#fazer o negocio de string uper e lower

#variaveis/listas
listaDeAlunos = []  # VAI ARMAZENAR AS CLASSES DAS PESSOAS
listaDeTreino = [] #VAI SER UMA MATRIZ, O NOME VAI PELO NUMERO E OS EX SERÃO CLASSES
listadnome = []  # VAI ARMAZENAR SÓ OS NOMES E SUAS POSIÇÕES


barra = "===================================================="
barra2 = "----------------------------------------------------"
inputer = "==> "

#----------------------------------------------------------------------------------------------#


#classe aluno
class Aluno:
    nome = None
    cpf = None
    peso = None
    altura = None
    numero = None
    status = False
    treino = []

    def __init__(self, name, cppf, weit, baixura):
        self.nome = name
        self.cpf = cppf
        self.peso = weit
        self.altura = baixura

#----------------------------------------------------------------------------------------------#
#classe exercicios
class Exer:
    nome = None
    numeroDeRepeticao = 0
    carga = 0

    def __init__(self, name, rep, carg):
        self.nome = name
        self.numeroDeRepeticao = rep
        self.carga = carg


#----------------------------------------------------------------------------------------------#
#funções

#ajuda
def ajuda():
    print(barra)
    print("lista de comandos:")
    print("Digite 0 para encerrar o programa")
    print("Digite 1 para: cadastrar aluno(a)")
    print("Digite 2 para: Gerenciar treino")
    print("Digite 3 para: Consultar aluno(a)")
    print("Digite 4 para: Atualizar cadastro do aluno(a)")
    print("Digite 5 para: Excluir aluno(a)")
    print("Digite 6 para: Relatório de alunos(as)")
    print("Digite 7 para: mudar as barras do site")
    menu()


#----------------------------------------------------------------------------------------------#
#pegando info
def info():
    while True:
        novoAluno = str(input(inputer))
        if novoAluno in listadnome:
            print("Nome repetido, insira outro")
        elif novoAluno == "0":
            menu()
        else:
            break

    print("Insira o CPF do aluno(a):")
    cpf = quebrafloat()


        # peso
    print("Insira o peso do aluno(a) em Kgs:")
    peso = quebrafloat()

        # Altura
    print("Insira a altura do aluno(a) em centimetros:")
    altura = quebrafloat()

    return(novoAluno, cpf, peso, altura)


#----------------------------------------------------------------------------------------------#
#adicionar aluno
def adicionaraluno():

    novoAluno, cpf, peso, altura = info()

    pessoa = Aluno(novoAluno, cpf, peso, altura)
    listaDeAlunos.append(pessoa) #CRIA UMA CLASSE
    listaDeTreino.append([])#CRIADA PELO INDEX DELA
    listadnome.append(novoAluno) #O NOME PRA N REPETIR

    #novoAluno = [] #stringa para botar os treinos

    print("Aluno(a) adicionado com sucesso!")


#----------------------------------------------------------------------------------------------#
#fun pra mudar o layout
def mudarbarras():
    global inputer
    global barra
    global barra2
    print("Escreva como você prefere a barra grossa:")
    barra = str(input(inputer))
    print("Escreva como você prefere a barra fina:")
    barra2 = str(input(inputer))
    print("Escreva como você prefere a caixa de texto:")
    inputer = str(input(inputer))

    return()

#----------------------------------------------------------------------------------------------#
#função conferir se não vai quebrar
def quebrafloat():
    while True:
        entrada = str(input(inputer))
        novo = entrada.upper()
        novo2 = entrada.lower()
        if entrada == "0":
            menu()

        if novo != entrada or novo2 != entrada:
            print("Letras foram inseridas, tente novamente ou digite 0 para ir ao menu")

        else:
            letrastirar = " "
            for letra in letrastirar:
                if letra in entrada:
                    entrada = entrada.replace(letra, '')
            entrada = float(entrada)
            return (entrada)

#----------------------------------------------------------------------------------------------#
    #gerenciamento(1)
def gerenciamento():
    print(barra)
    print("Gerenciando treino:")
    print("Digite 1 para adicionar um exercício")
    print("Digite 2 para alterar um exercício existente")
    print("Digite 3 para excluir um exercício")
    print("Digite 4 para excluir um treino inteiro")
    print("Digite qualquer outra coisa para voltar")
    n2 = str(input(inputer))

        # adicionar exercicio
    if n2 == "1":
        adicionarexercicio()

    #mudar exercicio
    if n2 == "2":
        alterarexe()

    #deletar ex:
    if n2 == "3":
        removerexe()

    if n2 == "4":
        print("Insira o nome do aluno(a) que você deseja limpar o treino ou digite 0 para voltar")
        exibirnomes()
        while True:
            nome = str(input(inputer))
            if nome == "0":
                menu()

            elif nome in listadnome:
                aluno = listadnome.index(nome)
                limpartreino(aluno)
                menu()

            else:
                print("Nome não encontrado, tente novamente ou digite 0 para voltar")


#----------------------------------------------------------------------------------------------#
#removendo exe
def removerexe():
    if exibirnomes() == "0":
        menu()
    else:
        print("Qual o nome do aluno(a) que você deseja deletar um exercício? ou aperte 0 para cancelar")
    while True:
        id = str(input(inputer))

        if id == "0":
            print("Voltando")
            menu()
        if id in listadnome:
            print("Aluno(a) encontrado!")
            if exibirtreino(id) == "0":
                menu()
            print("Qual o numero do exercício que você deseja deletar? Aperte 0 para cancelar")

            ida = listadnome.index(id) #pegando o id

            break
        else:
            print("Aluno não encontrado, tente novamente")

    while True:
        n_treino = int(input(inputer))
        if n_treino == "0":
            menu()
        elif n_treino > len(listaDeTreino[ida]): #verifica
            print("Exercício não encontrado, tente novamente ou digite 0 para cancelar")
        else:
            n_treino -= 1
            b = listaDeTreino[ida][n_treino]


            listaDeTreino[ida].remove(b)
            print("Exercicio removido com exito!")

            if len(listaDeTreino[ida]) == 0: #para desligar aluno caso fique sem exercicios
                listaDeAlunos[ida].status = False

            break

 # ----------------------------------------------------------------------------------------------#


#função exibir nomes
def exibirnomes():
    comp = len(listadnome)
    print(barra)
    if comp == 0:
        print("Não existem alunos(as) cadastrados")

        menu()

    else:
        print("Lista de alunos(as)")
        for i in range(comp):
            print(f"Aluno(a) n{i + 1}: {listadnome[i]}")
        print(barra2)
# ----------------------------------------------------------------------------------------------#
#função limpar treino:

def limpartreino(aluno):
    listaDeTreino[aluno].clear()
    if listaDeAlunos[aluno].status == True:
        listaDeAlunos[aluno].status = False
        print("Treino deletado com exito")
    elif len(listaDeTreino[aluno]) == 0:
        print("O Aluno(a) está ligado porém sem treino")
    else:
        print("Aluno(a) já está sem treino e desligado")

#----------------------------------------------------------------------------------------------#

#função lista d nomes
def exibirnomesseparados(n):
    print(f"Aluno n{n+ 1}: {listadnome[n]}")
    return(listadnome[n])

#----------------------------------------------------------------------------------------------#

#funçao exibir treino:
def exibirtreino(aluno):

    id = listadnome.index(aluno)
    comprimento = len(listaDeTreino[id])
    if listaDeAlunos[id].status == False: # se ficar sem exercicio, mas só se tiver sido deletado
        print("Este aluno(a) não está com treino ativo no momento")
        print(barra2)
        return("0")
    elif comprimento > 0:
        print(f"Lista de exercícios de {aluno}:")
        for i in range(comprimento):  #printa cada exe de uma vez depois acaba a linha
            particular = listaDeTreino[id][i]
            print(f"exercício {i + 1}: {particular.nome}, Repetições: {particular.numeroDeRepeticao}, Carga: {particular.carga}")
            print(barra2)
    else:
        print("Ainda não existem exercícios para esse aluno(a)")
        print(barra2)
        return("0")

#--------------------------------------------------------#

#função pra adicionar exercicio
def adicionarexe(aluno):

        while True:

            id = listadnome.index(aluno)
            exe = str(input(inputer))
            if exe == "0":
                print("Voltando")
                menu()

            for i in range(len(listaDeTreino[id])):
                if exe == listaDeTreino[id][i].nome:
                    print("Nome ja existente, tente novamente ou digite 0 para cancelar")
                    break
            else:
                formar = True
                break
        # exe = Exer
        if formar == True:
            print("Quantas repetições devem ser feitas?")
            re = quebrafloat()
            print("Qual a carga?")
            ca = quebrafloat()
            return (exe, re, ca)

#----------------------------------------------------------------------------------------------#

#funçao add ex (1)
def adicionarexercicio():
    exibirnomes()
    print("Coloque o nome do aluno(a) para adicionar um exercicio ou digite 0 para cancelar:")
    aluno = checarnome()
    id = listadnome.index(aluno)
    print("Aluno(a) encotrado, digite o nome do exercício")
    exe, re, ca = adicionarexe(aluno)
    listaDeTreino[id].append(Exer(exe, re, ca))
    listaDeAlunos[id].status = True
    print("Exercício adicionado com exito")



    return
#----------------------------------------------------------------------------------------------#

#alterar exercicio(1)

def alterarexe():
    exibirnomes()
    print("Insira o nome do aluno(a) que você deseja mudar o exercício ou digite 0 para voltar:")
    aluno = checarnome()
    va = listadnome.index(aluno)
    cancelar = exibirtreino(aluno)
    if cancelar == "0":
        menu()

    print("Digite o numero do exercício que você deseja alterar ou 0 para voltar:")
    while True:
        exepramudar = quebrafloat()
        exepramudar = int(exepramudar)

        comprimento = len(listaDeTreino[va])
        if exepramudar == 0:
            menu()

        elif exepramudar > comprimento or exepramudar < 0:
            print("Exercicio não esta na lista ou é um numero valido, tente novamente ou digite 0 para voltar")
            continue

        else:
            print("Qual o nome do novo exercicio:")
            exe = str((input(inputer)))
            print("Quantas repetições:")
            while True:
                re = quebrafloat()
                re = int(re)
                if re <= 0:
                    print("numero invalido, insira novamente:")
                else:
                    break

            print("Qual a carga?")
            ca = quebrafloat()

            exepramudar = exepramudar - 1
            listaDeTreino[va][exepramudar] = Exer(exe, re, ca)
            print("Exercício alterado com exito")
            break
        break

           # voltador
#----------------------------------------------------------------------------------------------#
#olhando nome:
def checarnome():

    while True:
        nosmi = str(input(inputer))
        if nosmi == "0":
            print("Voltando")
            menu()

        elif nosmi not in listadnome:
            print("Nome não encontrado, tente novamente ou digite 0 para voltar")

        else:
            return(nosmi)

#----------------------------------------------------------------------------------------------#

#deletar
def deletarpessoa():
    nome = checarnome()
    id = listadnome.index(nome)
    print(f"Você tem certeza que deseja deletar o aluno {nome}? digite 1 caso sim")
    faz = str(input(inputer))
    if faz == "1":
       listadnome.remove(nome)
       listaDeAlunos.pop(id)
       listaDeTreino.pop(id) #testando
       print("Aluno(a) removido(a) com exito")

    else:
        print("Operação cancelada")
        menu()
#----------------------------------------------------------------------------------------------#

#consultando aluno
def consultandoaluno():
    n = checarnome()
    mostra(n)
    exibirtreino(n)

#----------------------------------------------------------------------------------------------#
#função pra printar os dados
def mostra(n):
    id = listadnome.index(n)
    print(f"Dados pessoas de {n}:")
    print(barra2)
    print(f"Nome: {listaDeAlunos[id].nome}")
    print(f"CPF: {listaDeAlunos[id].cpf:.0f}")
    print(f"Peso: {listaDeAlunos[id].peso:.2f} Kgs")
    print(f"Altura: {listaDeAlunos[id].altura} Cms")
    peso = listaDeAlunos[id].peso
    altura = listaDeAlunos[id].altura / 100
    imc = peso / (altura ** 2)
    print(f"IMC: {imc:.1f}")
    imc = imcfaixa(imc)
    print(f"Faixa de imc: {imc}")
    print(f"Numero no sistema: {id + 1}")
    print(f"Status de assinatura: {listaDeAlunos[id].status}")

#----------------------------------------------------------------------------------------------#

#calculo da faixa d imc
def imcfaixa(n):
    if n < 17:
        return ("Muito abaixo do peso")
    elif n < 18.49:
        return ("Abaixo do peso")
    elif n < 24.99:
        return ("Peso normal")
    elif n < 29.99:
        return ("Acima do peso")
    elif n < 34.99:
        return ("Obesidade I")
    elif n < 39.99:
        return ("Obesidade II (severa)")
    else:
        return ("Obesidade III (mórbida)")


# ----------------------------------------------------------------------------------------------#
#alterando cadastro:

def alterandocadastro():
    print("Digite o nome do aluno(a) que você deseja alterar o cadastro")
    exibirnomes()
    n = checarnome()
    print(f"digite 1 se você tem certeza que quer mudar o cadastro de {n}")  #confirmação
    m = str(input(inputer))

    if m == "1":
        id = listadnome.index(n)
        print("insira o novo nome do aluno(a)")   #mudando os dados
        nomea, cpf, peso, altura = info()
        listaDeAlunos[id].nome = nomea
        listaDeAlunos[id].cpf = cpf
        listaDeAlunos[id].peso = peso
        listaDeAlunos[id].altura = altura
        listadnome[id] = nomea
        print("Dados alterados com exito")
    else:
        menu()

#---------------------------------------------------------------------------#

#fun pra mostrar as listas
def listas():
    comp = len(listadnome)
    while True:
        n = str(input(inputer))
        if n == "0":
            menu()
        elif n == "1":
            print("Lista de nomes")
            exibirnomes()
            menu()

        elif n == "2":
            print("Lista de nomes e informações:")
            for i in range(comp):
                aluno = exibirnomesseparados(i)
                mostra(aluno)
                print(barra2)
            menu()

        elif n == "3":
            print("Lista de nomes e treino:")
            for i in range(comp):
                aluno = exibirnomesseparados(i)
                exibirtreino(aluno)
                print(barra2)
            menu()

        elif n == "4":
            print("Lista de nomes, informações e treino:")
            for i in range(comp):
                aluno = exibirnomesseparados(i)
                mostra(aluno)
                exibirtreino(aluno)
                # print(barra2)
            menu()

        else:
            print("Comando não reconhecido, tente novamene ou digite 0 para cancelar")
            continue

# ----------------------------------------------------------------------------------------------#

#menu
def menu():

    while True:
        print(barra)
        print("MENU INICIAL: para exibir a lista de comandos digite 8")
        n_inicial = str(input(inputer))

        #encerrar programa
        if n_inicial == "0":
            sys.exit()

        #comandos
        if n_inicial == "8":
            ajuda()


        #cadastrar alunos:
        elif n_inicial == "1":
            print(barra)
            print("Insira o nome do aluno(a) que você deseja adicionar:")
            adicionaraluno()


        # gerenciando treino:
        elif n_inicial == "2":
            gerenciamento()

        elif n_inicial == "3":
            exibirnomes()
            print("Digite o nome do aluno(a) que você deseja consultar ou 0 para voltar")
            consultandoaluno()

        elif n_inicial == "4":
            exibirnomes()
            alterandocadastro()

        elif n_inicial == "5":
            print("Qual aluno(a) você deseja excluir, ou aperte 0 para excluir:")
            exibirnomes()
            deletarpessoa()

        elif n_inicial == "6":
            print(barra)
            comp = len(listadnome) #comprimento
            if comp == 0:
                print("Ainda não tem alunos cadastrados")
                menu()
            print("Escolha quais informações você quer apresentar:")
            print("Digite 1 para apenas os nomes;")
            print("Digite 2 para nomes e cadastro;")
            print("Digite 3 para nomes e treinos; ")
            print("Digite 4 para nomes cadastros e treinos.")
            listas()

        elif n_inicial == "7":
            print("Configurações atuais:")
            print("Barra grossa:")
            print(barra)
            print()
            print("Barra fina:")
            print(barra2)
            print()
            print("Caixa de texto:")
            print(inputer)
            print()
            print("Digite 1 se quiser modificar as barras")
            fazer = str(input(inputer))
            if fazer == '1':
                mudarbarras()

            else:
                print("Operação cancelada")
                menu()

        elif n_inicial == "t":#TESTES
            exibirtreino(input())

        else:
            print(barra)
            print("comando não encontrado, tente novamente")


#inicio
print(barra)
print("Bem vindo ao gerenciador de treino: 💪 Abdomináveis 💪")
menu()