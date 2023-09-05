//fazer uma matriz q seja a linha x coluna
#include <stdio.h>

#define linha 5
#define coluna 5

void imprimirMatriz(int matriz[linha][coluna]);

int main()
{

    int matriz[linha][coluna];

    for (int l = 0; l < linha; l++)
    {
        for (int c=0; c<coluna; c++)
        {
            matriz[l][c] = (l+1)*(c+1);
        }
    }
    imprimirMatriz(matriz);
}
void imprimirMatriz(int matriz[linha][coluna])
{
    for (int l =0; l < linha; l++)
    {
        for (int c=0; c<coluna; c++)
        {
            printf("%d ", matriz[l][c]);
        }
        printf("\n");
    }
}