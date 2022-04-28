import pandas as pd

import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from tkinter import *
from tkinter import ttk



def formula_magica():
    s = Service('C:/Users/Robson/anaconda3/chromedriver.exe') #ALTERAR O CAMINHO
    driver = webdriver.Chrome(service=s)
    driver.get("https://statusinvest.com.br/acoes/busca-avancada")
    wait = WebDriverWait(driver, 10)
    try: #botão de busca
        busca = driver.find_element(By.XPATH, '//*[@id="main-2"]/div[3]/div/div/div/button[2]')
        busca.click()
    except TimeoutException as to:
        print('Tempo expirado, reinicie o programa')
        driver.close()
    try:  #analisa se o botão de fechar o popup aparece e clica em fechar
        popup = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-close')))
        popup.click()
    except TimeoutException as to:
        print('Tempo expirado, reinicie o programa')
        driver.close()
    try:  #analisa se o botão de download aparece e clica
        download = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-2"]/div[4]/div/div[1]/div[2]/a')))
        download.click()
    except TimeoutException as to:
        print('Tempo expirado, reinicie o programa')
        driver.close()
    sleep(5)  #tempo necessário para efetuar o download antes de fechar o navegador
    driver.close()

    #Move o arquivo da pasta Downloads para a pasta Databases
    atual = r'C:\Users\Robson\OneDrive\Downloads\statusinvest-busca-avancada.csv' #ALTERAR O CAMINHO
    caminhoDatabases = r'C:\Users\Robson\OneDrive\Documentos\Python\Mercado-Financeiro\Fórmula Mágica de Joel Greenblatt\Databases\statusinvest-busca-avancada'#ALTERAR O CAMINHO
    destino = caminhoDatabases + '.csv'
    shutil.move(atual, destino)

    #IMPORTANDO DADOS
    tabela = pd.read_csv(destino, sep=';', index_col=None, header=0, decimal=',', thousands='.')
    tabela.to_excel(caminhoDatabases + '.xlsx')
    tabela = pd.read_excel(caminhoDatabases + '.xlsx', decimal=',', thousands='.')

    #CRIANDO RANKING
    tabela = tabela[tabela[' LIQUIDEZ MEDIA DIARIA'] > 1000000]
    tabela = tabela[tabela['P/L'] > 0]
    ranking = pd.DataFrame()
    ranking['POS'] = range(1, 101)
    ranking['EV/EBIT'] = tabela[tabela['EV/EBIT'] > 0].sort_values(by=['EV/EBIT'])['TICKER'][:100].values
    ranking['ROIC'] = tabela[tabela['ROIC'] > 0].sort_values(by=['ROIC'], ascending=False)['TICKER'][:100].values

    #SOMANDO AS PONTUAÇÕES DO RANKING
    a = ranking.pivot_table(columns='EV/EBIT', values='POS')
    b = ranking.pivot_table(columns='ROIC', values='POS')
    t = pd.concat([a, b])
    rank = t.dropna(axis=1).sum()
    rank = rank.sort_values()[:10]
    print(rank)


janela = Tk()
frame = ttk.Frame(janela, padding=20)
frame.grid()
janela.title('Fórmula Mágica de Joel Greenblatt')
ttk.Label(frame, text='Olá, investidores!').grid(column=0, row=1)
ttk.Label(frame, text='Clique no botão pra rodar a Fórmula Mágica').grid(column=0, row=2)
ttk.Button(frame, text='Sair', command=janela.destroy).grid(column=1, row=1)
ttk.Button(frame, text='Rodar a Fórmula Mágica', command=formula_magica).grid(column=1, row=2)

janela.mainloop()
