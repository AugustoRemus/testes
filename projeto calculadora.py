while True:
    valor1 = float(input("insira o primeiro valor "))
    operacao = str(input("digite qual operação voce deseja fazer ou digite interrogação (?) para a lista de comandos "))
    valor2 = float(input("digite o segundo valor "))
    while True:
        if operacao == ("+"):
            resultado = valor1 + valor2
            break

        elif operacao == ("-"):
            resultado = valor1 - valor2
            break

        elif operacao == ("*") or operacao == ("x"):
            resultado = valor1 * valor2
            break

        elif operacao == (":"):
            resultado = valor1 / valor2
            break

        elif operacao == ("?"):
            print("adição: + \nsubtração: -\nmultiplicação: x ou *\ndivisão: :")
            operacao = str(input("qual operação quer fazer? "))
            continue
        else:
            print("operador não reconhecido")
            continue

    casasDecimais = int(input("quantas casas decimais voce quer? "))
    print(f"o seu resultado é {resultado:.{casasDecimais}f}")

#ai ai