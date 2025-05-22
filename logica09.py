import pandas as pd
import numpy as np

# Simulação de dados
dados = pd.DataFrame({
    'filial': ['SP', 'RJ', 'MG', 'SP', 'RJ', 'MG', 'SP', 'RJ', 'MG'],
    'mes': ['Jan', 'Jan', 'Jan', 'Fev', 'Fev', 'Fev', 'Mar', 'Mar', 'Mar'],
    'faturamento': [100000, 95000, 85000, 110000, 97000, 87000, 120000, 98000, 90000],
    'custo': [70000, 68000, 60000, 72000, 69000, 62000, 75000, 70000, 64000]
})

# Funções de análise
def calcular_lucro(df):
    df['lucro'] = df['faturamento'] - df['custo']
    return df

def crescimento_percentual(df):
    resultado = {}
    filiais = df['filial'].unique()
    for filial in filiais:
        dados_filial = df[df['filial'] == filial].reset_index(drop=True)
        crescimentos = []
        for i in range(1, len(dados_filial)):
            ant = dados_filial.loc[i - 1, 'faturamento']
            atual = dados_filial.loc[i, 'faturamento']
            cresc = ((atual - ant) / ant) * 100
            crescimentos.append(round(cresc, 2))
        resultado[filial] = crescimentos
    return resultado

def ranking_filiais(df):
    total_por_filial = df.groupby('filial')['lucro'].sum().sort_values(ascending=False)
    return total_por_filial.reset_index()

def filiais_em_risco(df, margem_minima=0.2, faturamento_minimo=90000):
    df['margem'] = (df['lucro'] / df['faturamento']).round(2)
    riscos = df[(df['margem'] < margem_minima) | (df['faturamento'] < faturamento_minimo)]
    return riscos[['filial', 'mes', 'faturamento', 'margem']]

# Execução manual
if __name__ == "__main__":
    dados = calcular_lucro(dados)
    print("Lucro por mês:\n", dados)
    print("\nCrescimento percentual:\n", crescimento_percentual(dados))
    print("\nRanking por lucro:\n", ranking_filiais(dados))
    print("\nFiliais em risco:\n", filiais_em_risco(dados))

# ==========================
# 🎯 Testes Unitários
# ==========================
import unittest

class TestAnaliseFinanceira(unittest.TestCase):
    
    def setUp(self):
        self.dados = pd.DataFrame({
            'filial': ['A', 'A', 'B', 'B'],
            'mes': ['Jan', 'Fev', 'Jan', 'Fev'],
            'faturamento': [100000, 120000, 95000, 90000],
            'custo': [80000, 85000, 70000, 68000]
        })
        self.dados = calcular_lucro(self.dados)

    def test_calculo_lucro(self):
        self.assertEqual(self.dados.loc[0, 'lucro'], 20000)
        self.assertEqual(self.dados.loc[1, 'lucro'], 35000)

    def test_crescimento_percentual(self):
        cresc = crescimento_percentual(self.dados)
        self.assertAlmostEqual(cresc['A'][0], 20.0)
        self.assertAlmostEqual(cresc['B'][0], -5.26, places=2)

    def test_ranking(self):
        ranking = ranking_filiais(self.dados)
        self.assertEqual(ranking.iloc[0]['filial'], 'A')

    def test_filiais_em_risco(self):
        riscos = filiais_em_risco(self.dados, margem_minima=0.25, faturamento_minimo=95000)
        self.assertTrue('B' in riscos['filial'].values)

# Executar os testes
