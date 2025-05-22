import math
import unittest

def resolver_equacao_segundo_grau(a, b, c):
    if a == 0:
        raise ValueError("O coeficiente 'a' não pode ser zero em uma equação do segundo grau.")
    
    delta = b**2 - 4*a*c

    if delta < 0:
        return "Sem raízes reais"
    elif delta == 0:
        x = -b / (2*a)
        return (x,)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return (x1, x2)

# Parte principal
if __name__ == "__main__":
    try:
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))

        resultado = resolver_equacao_segundo_grau(a, b, c)
        print(f"Resultado: {resultado}")
    except Exception as e:
        print(f"Erro: {e}")

# Testes unitários
class TestEquacaoSegundoGrau(unittest.TestCase):
    def test_duas_raizes_reais(self):
        resultado = resolver_equacao_segundo_grau(1, -3, 2)  # x² - 3x + 2 = 0 → x = 1 e x = 2
        self.assertAlmostEqual(resultado[0], 2.0)
        self.assertAlmostEqual(resultado[1], 1.0)

    def test_uma_raiz_real(self):
        resultado = resolver_equacao_segundo_grau(1, -2, 1)  # x² - 2x + 1 = 0 → x = 1
        self.assertEqual(resultado, (1.0,))

    def test_sem_raizes_reais(self):
        resultado = resolver_equacao_segundo_grau(1, 2, 5)  # x² + 2x + 5 = 0 → Δ < 0
        self.assertEqual(resultado, "Sem raízes reais")

    def test_a_zero(self):
        with self.assertRaises(ValueError):
            resolver_equacao_segundo_grau(0, 2, 1)

# Para rodar os testes:
# Salve este código como `equacao.py`
# Depois execute: python -m unittest equacao.py
