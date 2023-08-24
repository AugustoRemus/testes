#include <stdio.h>
int maior = -200000;
int menor = 200000;

void maiorMenor(int a);

int main()
{
    int lista[5];
    int numero;
    int contador = 0;

    while (contador < 5)
    {
        
        printf("insira o numero %d :\n", contador +1);
        scanf("%d", &numero);

        lista[contador] = numero;
        contador ++;

    }
    contador = 0;
    while (contador < 5)
    {
        printf("%d\n", lista[contador]);
        contador ++;

    }
    contador = 0;
    printf("os maiores e menores são:\n");
    while (contador < 5)
    {
        maiorMenor(lista[contador]);
        contador = contador +1;
    }
    printf("o maior é: %d\n", maior);
    printf("o menor é: %d\n", menor);
}
void maiorMenor(int a)
{
    if(a < menor)
    {
        menor = a;
    }
    if (a > maior)
    {
        maior = a;
    }
}