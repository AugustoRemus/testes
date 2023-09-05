// fazer uma matriz com a diagonal principal 1 e o resto 0 e imprimir
#include<stdio.h>
#define linha 5
#define coluna 5

void printarMatriz(int matriz[linha][coluna]);

int main(){
    int matriz[linha][coluna];

    for(int l=0; l<5; l++)
    {
        for(int c=0; c< 5; c++)
        {
            if (l == c)
                matriz[l][c] =1;
            else
                matriz[l][c] = 0;
        }

    }
    printarMatriz(matriz);
    
}
void printarMatriz(int matriz[linha][coluna])
{
     for(int l=0; l<5; l++)
    {
        for(int c=0; c< 5; c++)
        {
            printf("%d ", matriz[l][c]);
        }
        printf("\n");
    }
}
