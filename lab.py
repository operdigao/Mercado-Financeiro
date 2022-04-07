import pandas as pd
import shutil

atual = r'C:\Users\Robson\OneDrive\Downloads\statusinvest-busca-avancada.csv'
caminhoDatabases = r'C:\Users\Robson\OneDrive\Documentos\Python\Fortune Investimentos\Fórmula Mágica\Databases\statusinvest-busca-avancada'
destino = caminhoDatabases + '.csv'
shutil.move(atual, destino)

tabela = pd.read_csv(destino, sep=';', index_col=None, header=0, decimal=',', thousands='.')
tabela.to_excel(caminhoDatabases + '.xlsx')
tabela = pd.read_excel(caminhoDatabases + '.xlsx', decimal=',', thousands='.')
print(tabela)