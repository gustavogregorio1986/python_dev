import pandas as pd

def analisar_salarios(dados):
    """
    Função que analisa os salários de uma base de dados.
    Retorna a média, o desvio padrão e uma lista de salários fora do padrão (anomalias).
    """
    if 'salario' not in dados.columns:
        return "Coluna 'salario' não encontrada nos dados."

    media = dados['salario'].mean()
    desvio = dados['salario'].std()

    # Anomalias: salários muito fora da média (+/- 2 desvios padrão)
    anomalias = dados[dados['salario'] > media + 2*desvio]
    return {
        'media': round(media, 2),
        'desvio_padrao': round(desvio, 2),
        'anomalias': anomalias['salario'].tolist()
    }

# Execução manual
if __name__ == "__main__":
    # Simulando dados
    dados = pd.DataFrame({
        'nome': ['Ana', 'Carlos', 'Beatriz', 'João', 'Lucas'],
        'salario': [3000, 3200, 2900, 15000, 3100]
    })

    resultado = analisar_salarios(dados)
    print("Média Salarial:", resultado['media'])
    print("Desvio Padrão:", resultado['desvio_padrao'])
    print("Salários fora do padrão (anomalias):", resultado['anomalias'])

# Testes Unitários
import unittest

class TestAnaliseSalarios(unittest.TestCase):
    def test_analise_basica(self):
        df = pd.DataFrame({
            'nome': ['A', 'B', 'C'],
            'salario': [1000, 2000, 3000]
        })
        resultado = analisar_salarios(df)
        self.assertEqual(resultado['media'], 2000.0)
        self.assertEqual(round(resultado['desvio_padrao'], 2), 1000.0)
        self.assertEqual(resultado['anomalias'], [])

    def test_com_anomalia(self):
        df = pd.DataFrame({
            'nome': ['X', 'Y', 'Z', 'W'],
            'salario': [3000, 3200, 3100, 15000]
        })
        resultado = analisar_salarios(df)
        self.assertIn(15000, resultado['anomalias'])

    def test_coluna_inexistente(self):
        df = pd.DataFrame({
            'nome': ['A', 'B'],
            'idade': [25, 30]
        })
        resultado = analisar_salarios(df)
        self.assertEqual(resultado, "Coluna 'salario' não encontrada nos dados.")
