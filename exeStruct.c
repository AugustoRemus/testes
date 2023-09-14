#include <stdio.h>
#define and &&
#define or ||


typedef struct 
{
    int dia;
    int mes;
    int ano;
} Data;


void printarData(Data data);
void compararDatas(Data data1, Data data2);
Data criandoData();



int main()
{
    //Data data1 = {10, 10, 2004};
    
    //printarData(data1);
    //printf("\n");
    printf("insira o dia, o mes e o ano da primeira data (dia mes ano)\n");
    
    Data data2;
    data2 = criandoData();
    printf("insira o dia, o mes e o ano da segunda data (dia mes ano)\n");    
    Data data3;
    data3 = criandoData();
    
    compararDatas(data2, data3);

}


void printarData(Data data)
{
    printf("%d / %d / %d ", data.dia, data.mes, data.ano);
}

void compararDatas(Data data1, Data data2)
{
    
    if(data1.ano == data2.ano && data1.mes == data2.mes && data1.dia == data2.dia)
    {
        printf("sao a mesma data");
    }
        else if(data1.ano > data2.ano)
        {
            printf("%d / %d / %d ", data1.dia, data1.mes, data1.ano);
            printf("é a data mais nova");
        }
            else if(data1.mes > data2.mes)
            {
                printf("%d / %d / %d ", data1.dia, data1.mes, data1.ano);
                printf("é a data mais nova");
            }
                else if (data1.dia > data2.dia)
                {
                    printf("%d / %d / %d ", data1.dia, data1.mes, data1.ano);
                    printf("é a data mais nova");   
                }
                    else
                    {
                        printf("%d / %d / %d ", data2.dia, data2.mes, data2.ano);
                        printf("e a data mais nova");
                    }

    
}

Data criandoData()
{
    Data datacriada;
    
    scanf("%d %d %d", &datacriada.dia, &datacriada.mes, &datacriada.ano);
    return(datacriada);
    
}