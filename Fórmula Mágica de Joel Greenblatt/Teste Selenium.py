from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import shutil
import pandas as pd

#Acessa o site do StatusInvest e faz o download do arquivo csv das empresas
s = Service('C:/Users/Robson/anaconda3/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://statusinvest.com.br/acoes/busca-avancada")
driver.find_element(By.XPATH, '//*[@id="main-2"]/div[3]/div/div/div/button[2]').click() #botão de busca
wait = WebDriverWait(driver, 10)
try: #analisa se o botão de fechar o popup aparece e clica em fechar
    popup = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-close')))
    popup.click()
except TimeoutException as to:
    print('Tempo expirado, reinicie o programa')
    driver.close()
try:
    download = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-2"]/div[4]/div/div[1]/div[2]/a')))
    download.click()
except TimeoutException as to:
    print('Tempo expirado, reinicie o programa')
    driver.close()
sleep(5)
driver.close()

#Move o arquivo da pasta Downloads para a pasta Databases
atual = r'C:\Users\Robson\OneDrive\Downloads\statusinvest-busca-avancada.csv'
destino = r'C:\Users\Robson\OneDrive\Documentos\Python\Fórmula Mágica\Databases\statusinvest-busca-avancada.csv'
shutil.move(atual, destino)
"""#Converte o arquivo csv para xlsx
tabela = pd.read_csv(destino, sep=';', index_col=None, header=0)
tabela.to_excel(r'C:\Users\Robson\OneDrive\Documentos\Python\Fórmula Mágica\Databases\statusinvest-busca-avancada.xlsx')
print(tabela)"""
