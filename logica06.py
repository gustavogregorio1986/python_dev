def calcular_inss(salario):
    if salario <= 1320.00:
        return salario * 0.075
    elif salario <= 2571.29:
        return salario * 0.09
    else:
        return salario * 0.12

def calcular_fgts(salario):
    return salario * 0.08

def resumo_salario(salario):
    inss = calcular_inss(salario)
    fgts = calcular_fgts(salario)
    salario_liquido = salario - inss
    return {
        "salario_bruto": salario,
        "inss": round(inss, 2),
        "fgts": round(fgts, 2),
        "salario_liquido": round(salario_liquido, 2)
    }

# Exemplo de entrada do usuário
if __name__ == '__main__':
    try:
        salario = float(input("Digite o salário bruto: "))
        resultado = resumo_salario(salario)
        print(f"INSS: R$ {resultado['inss']}")
        print(f"FGTS: R$ {resultado['fgts']}")
        print(f"Salário Líquido: R$ {resultado['salario_liquido']}")
    except:
        print("Entrada inválida!")

# Testes unitários
import unittest

class TestCalculosSalario(unittest.TestCase):
    def test_inss_faixa_1(self):
        self.assertAlmostEqual(calcular_inss(1000), 75.00, places=2)

    def test_inss_faixa_2(self):
        self.assertAlmostEqual(calcular_inss(2000), 180.00, places=2)

    def test_inss_faixa_3(self):
        self.assertAlmostEqual(calcular_inss(3000), 360.00, places=2)

    def test_fgts(self):
        self.assertAlmostEqual(calcular_fgts(2500), 200.00, places=2)

    def test_resumo_salario(self):
        resumo = resumo_salario(3000)
        self.assertEqual(resumo['inss'], 360.00)
        self.assertEqual(resumo['fgts'], 240.00)
        self.assertEqual(resumo['salario_liquido'], 2640.00)

# Para rodar os testes, salve como arquivo .py e execute:
# python nome_do_arquivo.py
