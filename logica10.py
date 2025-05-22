import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import unittest

# Simular dados
dados = pd.DataFrame({
    'filial': ['SP', 'RJ', 'MG'] * 6,
    'mes': list(range(1, 7)) * 3,
    'faturamento': [100000, 90000, 85000, 110000, 95000, 87000,
                    120000, 97000, 89000, 125000, 99000, 91000,
                    130000, 101000, 92000, 135000, 103000, 94000],
    'custo': [70000, 65000, 60000, 72000, 67000, 62000,
              75000, 69000, 64000, 78000, 71000, 66000,
              80000, 73000, 68000, 82000, 75000, 70000]
})

# 1. Calcular lucro e margem
def calcular_lucro_margem(df):
    df['lucro'] = df['faturamento'] - df['custo']
    df['margem'] = (df['lucro'] / df['faturamento']).round(2)
    return df

# 2. Filiais em risco
def detectar_risco(df, margem_min=0.2):
    return df[df['margem'] < margem_min]

# 3. Previsão de faturamento futuro por filial
def prever_faturamento(df, filial, meses_futuros=2):
    dados_filial = df[df['filial'] == filial]
    X = dados_filial[['mes']]
    y = dados_filial['faturamento']
    modelo = LinearRegression().fit(X, y)
    futuras = pd.DataFrame({'mes': list(range(max(X['mes']) + 1, max(X['mes']) + 1 + meses_futuros))})
    futuras['previsao'] = modelo.predict(futuras[['mes']])
    return futuras

# 4. Ranking por lucro total
def ranking(df):
    return df.groupby('filial')['lucro'].sum().sort_values(ascending=False)

# 5. Gráfico da evolução de uma filial
def plotar_evolucao(df, filial):
    dados_filial = df[df['filial'] == filial]
    plt.plot(dados_filial['mes'], dados_filial['faturamento'], label='Faturamento')
    plt.plot(dados_filial['mes'], dados_filial['custo'], label='Custo')
    plt.title(f"Evolução: {filial}")
    plt.xlabel("Mês")
    plt.ylabel("R$ Valor")
    plt.legend()
    plt.grid()
    plt.show()

# Execução principal
if __name__ == '__main__':
    dados = calcular_lucro_margem(dados)
    print("Ranking de filiais:\n", ranking(dados))
    print("\nFiliais em risco:\n", detectar_risco(dados))
    print("\nPrevisão SP:\n", prever_faturamento(dados, 'SP'))

    plotar_evolucao(dados, 'SP')

# ===========================
# TESTES UNITÁRIOS
# ===========================
class TestFinanceiroComplexo(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'filial': ['SP', 'SP', 'RJ', 'RJ'],
            'mes': [1, 2, 1, 2],
            'faturamento': [100000, 110000, 90000, 95000],
            'custo': [70000, 72000, 65000, 67000]
        })
        self.df = calcular_lucro_margem(self.df)

    def test_lucro(self):
        self.assertEqual(self.df.loc[0, 'lucro'], 30000)
        self.assertEqual(self.df.loc[1, 'lucro'], 38000)

    def test_margem(self):
        self.assertAlmostEqual(self.df.loc[0, 'margem'], 0.3)
        self.assertAlmostEqual(self.df.loc[1, 'margem'], 0.35)

    def test_ranking(self):
        rank = ranking(self.df)
        self.assertEqual(rank.index[0], 'SP')

    def test_previsao_faturamento(self):
        previsao = prever_faturamento(self.df, 'SP', 1)
        self.assertTrue('previsao' in previsao.columns)

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
