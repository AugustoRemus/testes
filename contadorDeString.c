#include <stdio.h>

int func (char vetor[]);

int main()
{
    char lista[5] = {"nabo"};
    char lista2[100];

    scanf("%s", lista2);
    int c;

    c = func(lista2);

    
    printf("%d", c);

}

int func (char vetor[])
{
    int contador = 0;
    while (vetor[contador] != '\0')
    {   
        contador++;
    }
    return(contador);
}
