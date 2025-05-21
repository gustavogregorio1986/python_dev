nome = input('Digite o nome: ')                 # Solicita o nome
idade = int(input('Digite a idade: '))          # Solicita a idade e converte para inteiro

if idade >= 18:                                  # Verifica se é maior de idade
    print(f'O {nome} é maior de idade')         # Imprime se for maior
else:
    print(f'O {nome} é menor de idade')         # Imprime se for menor

