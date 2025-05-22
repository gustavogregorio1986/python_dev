def calcular_salario(nome, salario):
    if salario >= 9000:
        bonus = salario * 0.60
    elif salario >= 7000:
        bonus = salario * 0.40
    elif salario >= 6000:
        bonus = salario * 0.30
    elif salario >= 4000:
        bonus = salario * 0.10
    else:
        bonus = 0.0

    total = salario + bonus
    return f'O {nome} e o total do salario é: {total:.2f}'


# Entrada manual
if __name__ == '__main__':
    try:
        nome = input('Digite o nome: ')
        idade = int(input('Digite a idade: '))
        salario = float(input('Digite o salario: '))

        resultado = calcular_salario(nome, salario)
        print(resultado)
    except:
        print("Entrada inválida")

# Testes
import unittest

class TestCalcularSalario(unittest.TestCase):
    def test_salario_9500(self):
        self.assertEqual(calcular_salario('João', 9500), 'O João e o total do salario é: 15200.00')

    def test_salario_7000(self):
        self.assertEqual(calcular_salario('Ana', 7000), 'O Ana e o total do salario é: 9800.00')

    def test_salario_6000(self):
        self.assertEqual(calcular_salario('Carlos', 6000), 'O Carlos e o total do salario é: 7800.00')

    def test_salario_4000(self):
        self.assertEqual(calcular_salario('Lúcia', 4000), 'O Lúcia e o total do salario é: 4400.00')

    def test_salario_3000(self):
        self.assertEqual(calcular_salario('Pedro', 3000), 'O Pedro e o total do salario é: 3000.00')
