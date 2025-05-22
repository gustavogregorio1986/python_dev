import unittest

def tabuada(numero):
    """
    Gera a tabuada do número fornecido, de 1 a 10.
    Retorna uma string com cada linha no formato:
      "numero x i = resultado"
    """
    linhas = []
    for i in range(1, 11):
        linhas.append(f"{numero} x {i} = {numero * i}")
    return "\n".join(linhas)

# Bloco de execução manual (apenas se não estiver rodando os testes)
if __name__ == '__main__':
    # Verifica se o usuário deseja executar os testes ou usar a função manualmente
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "teste":
        unittest.main(argv=[sys.argv[0]])
    else:
        numero = int(input("Digite um número para gerar a tabuada: "))
        print(tabuada(numero))
    
# Testes Unitários
class TestTabuada(unittest.TestCase):
    def test_tabuada_do_2(self):
        esperado = (
            "2 x 1 = 2\n"
            "2 x 2 = 4\n"
            "2 x 3 = 6\n"
            "2 x 4 = 8\n"
            "2 x 5 = 10\n"
            "2 x 6 = 12\n"
            "2 x 7 = 14\n"
            "2 x 8 = 16\n"
            "2 x 9 = 18\n"
            "2 x 10 = 20"
        )
        self.assertEqual(tabuada(2), esperado)

    def test_tabuada_do_0(self):
        esperado = "\n".join([f"0 x {i} = 0" for i in range(1, 11)])
        self.assertEqual(tabuada(0), esperado)
