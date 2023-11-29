import pandas as pd

#   Criando um arquivo excel
carteira = {'Ativos':['BOVA11', 'MGLU3', 'BBDC4', 'ITUB4', 'ENEV3', 'MOVI3', \
                       'BPAC11', 'BCRI11', 'VILG11', 'KNRI11', 'XPLG11'], \
            'Tipo':['ETF', 'Ação', 'Ação', 'Ação', 'Ação', 'Ação', \
                     'Ação', 'FII', 'FII', 'FII', 'FII'], \
            'Qtde':[100, 1000, 100, 100, 300, 100, 100, 100, 100, 100, 100,]
            }

carteira_df = pd.DataFrame(carteira)
carteira_df.to_excel('carteira.xlsx', index=False)
