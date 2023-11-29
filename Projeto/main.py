import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas_datareader import data as pdr
import yfinance as ifin

carteira = pd.read_excel('carteira.xlsx')
ifin.pdr_override()

cotacoes_carteira = pd.DataFrame()
for ativo in carteira['Ativos']:
    cotacoes_carteira[ativo] = pdr.DataReader('{}.SA'.format(ativo), start='2020-01-01', end='2020-11-10')['Adj Close']


#       Ajustando os dados(Tratando Problemas de Importação pro DataFrame e Normalização)

#  Preencher com a média da coluna
"""df_media = cotacoes_carteira.mean()
cotacoes_carteira = cotacoes_carteira.fillna(df_media)"""

#  Preencher com o próximo valor não vazio da sequência
cotacoes_carteira = cotacoes_carteira.bfill()

cotacoes_carteira.info()

#   Como Que As Ações Foram Individualmente
carteira_nom = cotacoes_carteira / cotacoes_carteira.iloc[0]
# Gráfico
carteira_nom.plot(figsize=(15, 5))
plt.legend(loc='upper left')
plt.show()
