import pandas as pd
import warnings
import requests
from interface import *

warnings.filterwarnings('ignore')
cabeçalho('IMPORTANDO DADOS DAS EMPRESAS')
url = 'http://www.fundamentus.com.br/resultado.php'
header = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"  
 }
r = requests.get(url, headers=header)
tabela = pd.read_html(r.text,  decimal=',', thousands='.')[0]
print(tabela)

for coluna in ['Div.Yield', 'Mrg Ebit', 'Mrg. Líq.', 'ROIC', 'ROE', 'Cresc. Rec.5a']:
  tabela[coluna] = tabela[coluna].str.replace('.', '')
  tabela[coluna] = tabela[coluna].str.replace(',', '.')
  tabela[coluna] = tabela[coluna].str.rstrip('%').astype('float') / 100

cabeçalho('FILTRANDO EMPRESAS')
#liq = int(input('Qual a liquidez média diária mínima você deseja? '))
tabela = tabela[tabela['Liq.2meses'] > 1000000] #liq
#pl = int(input('Qual o P/L mínimo? '))
tabela = tabela[tabela['P/L'] > 0] #pl

cabeçalho('CRIANDO RANKING')
ranking = pd.DataFrame()
ranking['pos'] = range(1, 101)
ranking['EV/EBIT'] = tabela[tabela['EV/EBIT'] > 0].sort_values(by=['EV/EBIT'])['Papel'][:100].values
ranking['ROIC'] = tabela[tabela['ROIC'] > 0].sort_values(by=['ROIC'], ascending=False)['Papel'][:100].values
print(ranking)

cabeçalho('SOMANDO AS PONTUAÇÕES DO RANKING')
a = ranking.pivot_table(columns='EV/EBIT', values='pos')
b = ranking.pivot_table(columns='ROIC', values='pos')
t = pd.concat([a,b])
rank = t.dropna(axis=1).sum()
print(rank)

cabeçalho('RANKING FINAL DA FÓRMULA MÁGICA')
print(rank.sort_values()[:13])
