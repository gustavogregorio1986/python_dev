import unittest

# Função principal
def verificar_numero(numero):
    if numero > 20:
        return f'O {numero} é maior que 20'
    else:
        return f'O {numero} é menor que 20'

# Entrada do usuário (executa apenas se não estiver rodando os testes)
if __name__ == '__main__':
    try:
        numero = int(input('Digite o número: '))
        resultado = verificar_numero(numero)
        print(resultado)
    except:
        print("Entrada inválida")

# Classe de teste
class TestVerificarNumero(unittest.TestCase):
    def test_maior_que_20(self):
        self.assertEqual(verificar_numero(25), 'O 25 é maior que 20')

    def test_menor_que_20(self):
        self.assertEqual(verificar_numero(10), 'O 10 é menor que 20')

    def test_igual_a_20(self):
        self.assertEqual(verificar_numero(20), 'O 20 é menor que 20')

