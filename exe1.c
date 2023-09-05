// imprime a diagonal principal
#include <stdio.h>
#define linha 4
#define coluna 4
void imprimirDiagonal(int matriz[4][4]);
int main()
{

    int matriz[linha][coluna] = {
    
        {1, 2, 3, 4},
        {1, 2, 3, 4},
        {1, 2, 3, 4},
        {1, 2, 3, 4},
        }
    ;

    imprimirDiagonal(matriz);
}
void imprimirDiagonal(int matriz[4][4])
{
    for (int i = 0; i <4;i++)
            {printf("%d\n", matriz[i][i]);
            for (int d = -1; d<i; d ++)
            {
                printf(" ");
            }}

       


}