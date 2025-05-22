# funcionario.py

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_total_com_bonus(self):
        if self.salario >= 9000:
            bonus = self.salario * 0.60
        elif self.salario >= 7000:
            bonus = self.salario * 0.40
        elif self.salario >= 6000:
            bonus = self.salario * 0.30
        elif self.salario >= 4000:
            bonus = self.salario * 0.10
        else:
            bonus = 0.0

        total = self.salario + bonus
        return f'O {self.nome} e o total do salario é: {total:.2f}'


# Entrada manual
if __name__ == '__main__':
    try:
        nome = input('Digite o nome: ')
        idade = int(input('Digite a idade: '))
        salario = float(input('Digite o salario: '))

        funcionario = Funcionario(nome, salario)
        print(funcionario.calcular_total_com_bonus())
    except:
        print("Entrada inválida")


# testes_unitarios.py
import unittest

class TestFuncionario(unittest.TestCase):
    def test_salario_9500(self):
        f = Funcionario('João', 9500)
        self.assertEqual(f.calcular_total_com_bonus(), 'O João e o total do salario é: 15200.00')

    def test_salario_7000(self):
        f = Funcionario('Ana', 7000)
        self.assertEqual(f.calcular_total_com_bonus(), 'O Ana e o total do salario é: 9800.00')

    def test_salario_6000(self):
        f = Funcionario('Carlos', 6000)
        self.assertEqual(f.calcular_total_com_bonus(), 'O Carlos e o total do salario é: 7800.00')

    def test_salario_4000(self):
        f = Funcionario('Lúcia', 4000)
        self.assertEqual(f.calcular_total_com_bonus(), 'O Lúcia e o total do salario é: 4400.00')

    def test_salario_3000(self):
        f = Funcionario('Pedro', 3000)
        self.assertEqual(f.calcular_total_com_bonus(), 'O Pedro e o total do salario é: 3000.00')
