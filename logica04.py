numero1 = float(input('Digite o numero1: '))
numero2 = float(input('Digite o numero2: '))

print("\nEscolha a opção:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite o número da operação desejada: ")

# Verifica a operação escolhida
if opcao == "1":
    resultado = numero1 + numero2
    print(f"\nResultado da soma: {resultado}")
elif opcao == "2":
    resultado = numero1 - numero2
    print(f"\nResultado da subtração: {resultado}")
elif opcao == "3":
    resultado = numero1 * numero2
    print(f"\nResultado da multiplicação: {resultado}")
elif opcao == "4":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"\nResultado da divisão: {resultado}")
    else:
        print("\nErro: divisão por zero!")
else:
    print("\nOpção inválida.")