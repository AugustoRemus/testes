#include<stdio.h>
#include<string.h>

typedef struct 
{
    int matricula;
    int nota1;
    int nota2;
    int nota3;
    char nome[100];

} Aluno;

Aluno criarAluno();

int main()
{
    printf("insira o primeiro aluno\n");
    Aluno aluno1;
    aluno1 = criarAluno();
    

}
Aluno criarAluno()
{
    Aluno aluno1;

    printf("insira a matricula\n");
    scanf("%d", &aluno1.matricula);

    printf("insira o nome\n");
    scanf("%s", &aluno1.nome);

    printf("insira a primeira nota dele\n");
    scanf("%d", &aluno1.nota1);

    printf("insir a segunda nota\n");
    scanf("%d", &aluno1.nota2);

    printf("insira a terceira nota dele\n");
    scanf("%d", &aluno1.nota3);

    
    snprintf(aluno1.nome, sizeof(aluno1.nome),"%s",aluno1.nome);
    printf("nome: %s\nmatricula: %d, notas: %d %d %d", aluno1.nome, aluno1.matricula, aluno1.nota1, aluno1.nota2, aluno1.nota3);
    return(aluno1);
    


}
