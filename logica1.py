nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))
sexo = input('Digite o sexo: ')

if(idade >= 18) and (sexo == 'm'):
    print(f'{nome} pode se alistar')
else:
    print(f'{nome} não pode se alistar')