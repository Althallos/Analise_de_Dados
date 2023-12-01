import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as ifin

carteira = pd.read_excel('carteira.xlsx')
ifin.pdr_override()

cotacoes_carteira = pd.DataFrame()
for ativo in carteira['Ativos']:
    cotacoes_carteira[ativo] = pdr.DataReader('{}.SA'.format(ativo), start='2020-01-01', end='2020-11-10')['Adj Close']


#   Ajustando os dados(Tratando Problemas de Importação pro DataFrame e Normalização)

cotacoes_carteira.info()
#  Preencher com a média da coluna
"""df_media = cotacoes_carteira.mean()
cotacoes_carteira = cotacoes_carteira.fillna(df_media)"""
#  Preencher com o próximo valor não vazio da sequência
cotacoes_carteira = cotacoes_carteira.bfill()
cotacoes_carteira.info()


#   Como Que As Ações Foram Individualmente
carteira_nom = cotacoes_carteira / cotacoes_carteira.iloc[0]
#   Gráfico
carteira_nom.plot(figsize=(15, 5))
plt.legend(loc='upper left')
plt.show()


#   Criando um DataFrame da Carteira com as quantidades de ações
valor_investido = pd.DataFrame()
for ativo in carteira['Ativos']:
    valor_investido[ativo] = cotacoes_carteira[ativo] * carteira.loc[carteira['Ativos']==ativo, 'Qtde'].values[0]
valor_investido['Total'] = valor_investido.sum(axis=1)
print(valor_investido)