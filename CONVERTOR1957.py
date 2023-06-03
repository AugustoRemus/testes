def fazer(c):
    resultado = ""

    if c == 0:
        print("0")

    while c > 0:
        resto = c % len(nu)
        resultado = nu[resto] + resultado
        c = c // len(nu)
    return resultado






print("insira o numero da base:")
n = int(input())
base = n

sequencia = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
nu = ""

while n > 0:
    n = n - 1
    nu = sequencia[n] + nu

print(f"sequencia de digitos da base: {nu}")
print()
while True:

    print(f"insira o numero para converter para {base}")

    p = int(input())

    print(f"o numero decimal: {p} em base {base} é:")
    print(fazer(p))
    print("====================================================")

    print()


#versão 0.01
#made by gustavo limarrr

