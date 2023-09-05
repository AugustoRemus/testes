// acha o maior e menor numero da matriz e mostra a cordenada
#include <stdio.h>
#define linha 4
#define coluna 4

void maiorProcurar (int matriz[linha][coluna]);
int main()
{

    int matriz[linha][coluna] =
    {
        {3, 4, 5, 6},
        {4, 4, 5, 6},
        {3, 5, 5, 6},
        {3, 4, 5, 7},
    };
    maiorProcurar(matriz);
}
void maiorProcurar (int matriz[linha][coluna])
{
    int maior = -99999999;
    int linhaMaior;
    int colunaMaior;

    int menor = 999999999;
    int linhaMenor;
    int colunaMenor;

    for (int l =0; l < linha; l++)
        {
        for (int c =0; c< coluna; c++)
            {
                if(matriz[l][c]< menor)
                {
                    menor = matriz[l][c];
                    linhaMenor = l;
                    colunaMenor = c;
                }
                
                if(matriz[l][c]> maior)
                {
                    maior = matriz[l][c];
                    linhaMaior = l;
                    colunaMaior = c;
                }
            }
        }
        printf("maior numero = %d\n", maior);
        printf("cordenada do maior numero = %d, %d\n", linhaMaior + 1, colunaMaior +1);
        printf("menor numero = %d\n", menor);
        printf("cordenada do maior numero = %d, %d\n", linhaMenor +1, colunaMenor + 1);
}