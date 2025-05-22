def votar_papa(votos, nome_papa):
    """Adiciona um voto para o Papa especificado no dicionário votos"""
    if nome_papa in votos:
        votos[nome_papa] += 1
    else:
        votos[nome_papa] = 1
    return votos

def papa_mais_votado(votos):
    """Retorna o nome do Papa com mais votos"""
    if not votos:
        return None
    return max(votos, key=votos.get)

# Programa principal - entrada manual (exemplo)
if __name__ == '__main__':
    votos = {}
    while True:
        nome = input("Digite o nome do Papa para votar (ou 'fim' para encerrar): ")
        if nome.lower() == 'fim':
            break
        votos = votar_papa(votos, nome)
    melhor_papa = papa_mais_votado(votos)
    if melhor_papa:
        print(f"O Papa mais votado foi: {melhor_papa} com {votos[melhor_papa]} votos.")
    else:
        print("Nenhum voto registrado.")

# Testes unitários
import unittest

class TestVotacaoPapa(unittest.TestCase):
    def test_votar_papa(self):
        votos = {}
        votos = votar_papa(votos, "João Paulo II")
        votos = votar_papa(votos, "João Paulo II")
        votos = votar_papa(votos, "Bento XVI")
        self.assertEqual(votos["João Paulo II"], 2)
        self.assertEqual(votos["Bento XVI"], 1)

    def test_papa_mais_votado(self):
        votos = {"João Paulo II": 3, "Bento XVI": 1}
        self.assertEqual(papa_mais_votado(votos), "João Paulo II")

    def test_papa_mais_votado_vazio(self):
        votos = {}
        self.assertIsNone(papa_mais_votado(votos))

    def test_empate(self):
        votos = {"João Paulo II": 2, "Bento XVI": 2}
        # Em caso de empate, retorna o primeiro com maior valor encontrado
        self.assertIn(papa_mais_votado(votos), votos.keys())

# Para rodar os testes, execute:
# python -m unittest nome_do_arquivo.py
