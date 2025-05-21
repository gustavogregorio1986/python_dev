numero = int(input('Digite o numero: '))

for i in range(1, numero + 1):
    if( i % 2 == 0):
        print(f'O {i} é par!')
    else:
        print(f'O {i} é impar')