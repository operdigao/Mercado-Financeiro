import pandas as pd
import requests
from bs4 import BeautifulSoup
from lib.interface import *

cabeçalho('IMPORTANDO DADOS DAS EMPRESAS')
url = 'http://www.fundamentus.com.br/resultado.php'
header = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
site = requests.get(url, headers=header)
tabela = pd.read_html(site.text, decimal=',', thousands='.')[0]
for coluna in ['Div.Yield', 'Mrg Ebit', 'Mrg. Líq.', 'ROIC', 'ROE', 'Cresc. Rec.5a']:
  tabela[coluna] = tabela[coluna].str.replace('.', '')
  tabela[coluna] = tabela[coluna].str.replace(',', '.')
  tabela[coluna] = tabela[coluna].str.rstrip('%').astype('float') / 100
print(tabela)
