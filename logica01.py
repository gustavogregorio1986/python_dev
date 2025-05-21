nome = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a nota1: '))
nota2 = float(input('Digite a nota2: '))

mediaAluno = (nota1 + nota2)/2;

if (mediaAluno >= 7.0):
    print(f'{nome} esta aprovado')
elif (mediaAluno < 7.0) and (mediaAluno >= 3.0):
    print(f'{nome} esta em recuperação')
    recuperacao = float(input('Digite a nota de recuperacao: '))
    media = (mediaAluno + recuperacao)/2
    if(media >= 5.0):
        print(f'{nome} é aprovado!')
    else:
        print(f'{nome} é reprovado!')
else:
    print(f'{nome} esta reprovado')
