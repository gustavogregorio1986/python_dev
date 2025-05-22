def status_aluno(nota):
    """
    Recebe a nota do aluno e retorna:
    - 'Aprovado' se nota >= 7
    - 'Recuperação' se 5 <= nota < 7
    - 'Reprovado' se nota < 5
    """
    if nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

# Programa principal (exemplo de uso)
if __name__ == "__main__":
    try:
        nota = float(input("Digite a nota do aluno: "))
        resultado = status_aluno(nota)
        print(f"O aluno está: {resultado}")
    except ValueError:
        print("Por favor, digite um número válido para a nota.")

# Testes unitários
import unittest

class TestStatusAluno(unittest.TestCase):
    def test_aprovado(self):
        self.assertEqual(status_aluno(7), "Aprovado")
        self.assertEqual(status_aluno(8.5), "Aprovado")
        self.assertEqual(status_aluno(10), "Aprovado")

    def test_recuperacao(self):
        self.assertEqual(status_aluno(5), "Recuperação")
        self.assertEqual(status_aluno(6.9), "Recuperação")

    def test_reprovado(self):
        self.assertEqual(status_aluno(4.9), "Reprovado")
        self.assertEqual(status_aluno(0), "Reprovado")

# Para rodar os testes: python -m unittest nome_do_arquivo.py
