# analise_vendas.py

from statistics import mean, stdev, variance
from collections import defaultdict

# Dados de vendas: cada item é (cliente, produto, quantidade, preço unitário, custo unitário, região)
vendas = [
    ('João', 'Notebook', 2, 2500, 1800, 'Sudeste'),
    ('Maria', 'Smartphone', 1, 1500, 1000, 'Sul'),
    ('Carlos', 'Notebook', 1, 2500, 1800, 'Sudeste'),
    ('Ana', 'Tablet', 3, 1200, 900, 'Nordeste'),
    ('Roberta', 'Smartphone', 2, 1500, 1000, 'Sul'),
    ('Bruno', 'Notebook', 1, 2500, 1800, 'Centro-Oeste'),
    ('Fernanda', 'Tablet', 2, 1200, 900, 'Nordeste'),
    ('João', 'Smartphone', 1, 1500, 1000, 'Sudeste'),
]

# Funções de análise
def faturamento_por_regiao(vendas):
    resultado = defaultdict(float)
    for cliente, produto, qtd, preco, custo, regiao in vendas:
        resultado[regiao] += qtd * preco
    return dict(resultado)

def produto_mais_vendido_por_regiao(vendas):
    resultado = defaultdict(lambda: defaultdict(int))
    for _, produto, qtd, _, _, regiao in vendas:
        resultado[regiao][produto] += qtd
    return {regiao: max(produtos, key=produtos.get) for regiao, produtos in resultado.items()}

def ticket_medio(vendas):
    clientes = set()
    total_vendas = 0
    for cliente, _, qtd, preco, *_ in vendas:
        clientes.add(cliente)
        total_vendas += qtd * preco
    return total_vendas / len(clientes)

def margem_lucro_por_produto(vendas):
    resultado = defaultdict(lambda: {'lucro': 0, 'qtd': 0})
    for _, produto, qtd, preco, custo, _ in vendas:
        resultado[produto]['lucro'] += (preco - custo) * qtd
        resultado[produto]['qtd'] += qtd
    return {p: round(v['lucro'] / v['qtd'], 2) for p, v in resultado.items()}

def estatisticas_precos(vendas):
    precos = [preco for _, _, _, preco, _, _ in vendas]
    return {
        'media': mean(precos),
        'desvio_padrao': stdev(precos),
        'variancia': variance(precos)
    }

# Execução
if __name__ == "__main__":
    print("Faturamento por região:", faturamento_por_regiao(vendas))
    print("Produto mais vendido por região:", produto_mais_vendido_por_regiao(vendas))
    print("Ticket médio por cliente: R$", ticket_medio(vendas))
    print("Margem de lucro por produto:", margem_lucro_por_produto(vendas))
    print("Estatísticas de preço unitário:", estatisticas_precos(vendas))

# Testes unitários
import unittest

class TestAnaliseVendas(unittest.TestCase):

    def test_faturamento_por_regiao(self):
        resultado = faturamento_por_regiao(vendas)
        self.assertAlmostEqual(resultado['Sudeste'], 2*2500 + 1*2500 + 1*1500)

    def test_produto_mais_vendido(self):
        resultado = produto_mais_vendido_por_regiao(vendas)
        self.assertEqual(resultado['Sul'], 'Smartphone')
        self.assertEqual(resultado['Nordeste'], 'Tablet')

    def test_ticket_medio(self):
        self.assertAlmostEqual(ticket_medio(vendas), 13500 / 6, places=2)

    def test_margem_lucro_por_produto(self):
        resultado = margem_lucro_por_produto(vendas)
        self.assertEqual(resultado['Notebook'], 700.0)
        self.assertEqual(resultado['Smartphone'], 500.0)

    def test_estatisticas_precos(self):
        stats = estatisticas_precos(vendas)
        self.assertTrue(stats['media'] > 1000)
        self.assertTrue(stats['desvio_padrao'] > 0)

