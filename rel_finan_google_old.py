from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import os
from bs4 import BeautifulSoup
#import matplotlib.pyplot as plt
#from twilio.rest import Client
import datetime
#import vonage
import requests
#from requests.auth import HTTPBasicAuth
import smtplib

def ajusta_caracteres(coluna):
    mapeamento = {
        'á': 'a', 'ã': 'a', 'é': 'e', 'ê': 'e', 'í': 'i', 'ó': 'o', 'õ': 'o', 'ú': 'u',
        '-': '_', ' ': '_', 'flamengo_rj': 'flamengo', 'atletico_pr': 'athletico_pr',
        'sport_recife': 'sport', 'chapecoense_sc': 'chapecoense'
    }
    for k, v in mapeamento.items():
        coluna = coluna.str.replace(k, v)
    return coluna.str.lower()

def classificar_despesa(descricao):
    # Crie uma função para classificar as despesas com base nos termos
    # Lógica de classificação
    if 'latam' in descricao or 'iberia' in descricao or 'unidas' in descricao or 'airbnb' in descricao or 'azul' in descricao or 'smiles' in descricao or 'gol' in descricao or 'city_hall' in descricao or 'foco_aluguel' in descricao or 'tam_lin' in descricao:
        return 'Viagem'
    elif 'buffet' in descricao or 'ifd' in descricao or 'convenie' in descricao or 'hot_dog' in descricao or 'rest' in descricao or 'food' in descricao or 'emporio' in descricao or 'mercad' in descricao or 'pao_de_açucar' in descricao or 'coffee' in descricao or 'casal_20' in descricao or 'panito' in descricao or 'sush' in descricao or 'sabor' in descricao or 'cheiro' in descricao or 'delicate' in descricao or 'mercear' in descricao or 'drink' in descricao or 'ilha_mix' in descricao or 'hermon' in descricao or 'tempero' in descricao or 'alimento' in descricao or 'suco' in descricao or 'megamatte' in descricao or 'chocolate' in descricao or 'rei_do_mate' in descricao or 'sunomono'  in descricao or 'padar' in descricao or 'lanch' in descricao or 'depos' in descricao or 'sams' in descricao or 'assai' in descricao or 'pao_de' in descricao or 'cafe' in descricao or 'ex_touro' in descricao or 'beco_do_espa' in descricao or 'rockribs' in descricao or 'daiso' in descricao or 'lulu' in descricao or 'mcdonald' in descricao or 'burger' in descricao or 'subway' in descricao or 'kfc' in descricao or 'bobs' in descricao or 'outback' in descricao or 'pizza' in descricao or 'boulevard_go' in descricao or 'starbuc' in descricao or 'cookie' in descricao or 'frutas' in descricao:
        return 'alimentacao'
    elif 'uber' in descricao or '99app' in descricao or 'estaciona' in descricao or 'posto' in descricao or 'conectcar' in descricao or 'tembici' in descricao or 'park' in descricao or 'barcas' in descricao or 'digipare' in descricao or 'auto_pos' in descricao:
        return 'Transporte'
    elif 'americanas' in descricao or 'renner' in descricao or 'pag*lojasrennersa' in descricao or 'iphone' in descricao or 'casa_e_vi' in descricao or 'relusa' in descricao or 'marketplace' in descricao or 'mr_cat' in descricao or 'cresci_e_perdi' in descricao or 'tonys_baby' in descricao or 'cirandinha_baby' in descricao or 'loungerie' in descricao or 'amazon' in descricao or 'shein' in descricao or 'calcad' in descricao:
        return 'Compras'
    elif 'netflix' in descricao or 'spotify' in descricao or 'apple_com/bill' in descricao or 'primebr' in descricao or 'doist' in descricao:
        return 'servicos'
    elif 'drog' in descricao or 'labora' in descricao:
        return 'saude'
    elif 'liberty' in descricao or 'calhas' in descricao or 'first_class' in descricao or 'chaveiro' in descricao or 'leroy' in descricao or 'lojas_g' in descricao or 'angela' in descricao or 'camica' in descricao or 'tok' in descricao or 'darkstore' in descricao:
        return 'Casa'
    elif 'infne' in descricao or 'cisco' in descricao:
        return 'educacao'
    elif 'funcional' in descricao:
        return 'esporte'
    elif 'beto_carrero' in descricao or 'ticket' in descricao:
        return 'diversao'    
    elif 'chic' in descricao or 'cabel' in descricao or 'sephora' in descricao or 'skin' in descricao or 'boticario' in descricao:
        return 'beleza' 
    elif 'anuid' in descricao:
        return 'anuidade'
    elif 'assb_comerci' in descricao or 'toy_boy' in descricao or 'kop' in descricao or 'happy' in descricao:
        return 'presente'
    else:
        return 'Outros'

def iniciar_driver():
    # Inicializa o driver do Selenium
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    #chrome_options.add_argument("--headless")  # Uncomment this line if you want to start Chrome in headless mode
    driver = uc.Chrome(use_subprocess=True, options=chrome_options)
    return driver

def obter_html(driver):
    try:
        # Abre a página de login do Mobills
        driver.get('https://web.mobills.com.br/auth/login')

        wait = WebDriverWait(driver, 30)
        #input("Pressione Enter para continuar...")

        # Localiza e clica no botão de login com o Google
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#signin_with > div > div > div'))).click()

        # Aguarda até que a página de login do Google seja carregada completamente
        time.sleep(1)

        windows = driver.window_handles
        driver.switch_to.window(windows[-1])

        email_gmail = os.getenv('EMAIL_GMAIL')
        senha_gmail = os.getenv('SENHA_GMAIL')
        # Insira seu e-mail do Google
        #email_gmail = "brunoropacheco@gmail.com"
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#identifierId'))).send_keys(email_gmail)
        
        # Clica no botão "Próxima"
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#identifierNext > div > button > span'))).click()

        # Aguarda até que a página de senha seja carregada completamente
        #time.sleep(3)
        #input("Pressione Enter para continuar...")

        # Insira sua senha do Google
        #senha_gmail           = "q0p!w9o@e8i#4&6"
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input'))).send_keys(senha_gmail)

        # Clica no botão "Próxima" para fazer login
        driver.find_element(By.CSS_SELECTOR, '#passwordNext > div > button > span').click()

        # Aguarda até que o login seja concluído
        #time.sleep(5)

        #opcao de smartphone ou tablet

        #wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > c-wiz > div > div.eKnrVb > div > div.j663ec > div > form > span > section:nth-child(2) > div > div > section > div > div > div > ul > li:nth-child(3) > div > div.vxx8jf'))).click()

        # Aguarda até que o login seja concluído

        #volta para a janela principal
        windows = driver.window_handles
        driver.switch_to.window(windows[0])
        time.sleep(5)
        
        #esperar aparecer o saldo atual na pagina de dashboard
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#dashboard-transactions-cards-accumuleted-balance > div')))
        
        # Após o login, redireciona para a página de transações
        driver.get('https://web.mobills.com.br/transactions')
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[1]/div/button/span[1]/h6')))

        # Aguarda um tempo para garantir que a página carregue completamente
        #time.sleep(10)
        input("Pressione Enter para continuar...")  
        
        # Check if it is after the 10th day of the month
        #print(datetime.datetime.now().day)
        if datetime.datetime.now().day >= 10:
            # Click on the "Next Month" button
            wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/main/div[2]/div[2]/div[1]/div/div[1]/div[2]/button[2]'))).click()
            # Wait for the page to load completely
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'table')))

            input("Pressione Enter para continuar...")
            
            # Get the HTML of the page again
            html_final = driver.page_source
        else:
            html_final = driver.page_source 
        
    finally:
    # Fecha o navegador
        driver.quit()
    #escrita do html em um arquivo
    with open('html_content.html', 'w') as file:
        file.write(html_final)
    return html_final

def processar_dados_sem_drive():
    #pega o html do arquivo ja pronto
    with open('html_content.html', 'r') as file:
        html = file.read()

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the table element
    table = soup.find('table')

    # Extract the data from the table
    data = []
    for row in table.find_all('tr'):
        row_data = [cell.get_text() for cell in row.find_all('td')]
        #print(row_data)
        if len(row_data) == 0:
            continue
        if row.find_all('td')[5].get('style')[11] == '7':
            row_data.append('receita')
        else: 
            row_data.append('despesa')
        if row.find_all('td')[2].find_all('span')[0].get('title') == None:
            data.append(row_data)
        else:
            row_data[2] = row.find_all('td')[2].find_all('span')[0].get('title')
            data.append(row_data)

    # Create a DataFrame from the data
    columns = ['Status', 'Dara', 'Descricao', 'Categoria', 'Conta', 'Valor', 'Acoes', 'RecXDes']
    df = pd.DataFrame(data, columns=columns)
    df.to_csv('transacoes.csv')
    return df

def processar_dados_com_drive(html):
    #pega o html do arquivo ja pronto
    #with open('html_content.html', 'r') as file:
    #    html = file.read()

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the table element
    table = soup.find('table')

    # Extract the data from the table
    data = []
    for row in table.find_all('tr'):
        row_data = [cell.get_text() for cell in row.find_all('td')]
        #print(row_data)
        if len(row_data) == 0:
            continue
        if row.find_all('td')[5].get('style')[11] == '7':
            row_data.append('receita')
        else: 
            row_data.append('despesa')
        if row.find_all('td')[2].find_all('span')[0].get('title') == None:
            data.append(row_data)
        else:
            row_data[2] = row.find_all('td')[2].find_all('span')[0].get('title')
            data.append(row_data)

    # Create a DataFrame from the data
    columns = ['Status', 'Dara', 'Descricao', 'Categoria', 'Conta', 'Valor', 'Acoes', 'RecXDes']
    df = pd.DataFrame(data, columns=columns)
    df.to_csv('transacoes.csv')
    return df

def ajustar_dataframe(df):
    # Remove as colunas 'Acoes' e 'Status'
    df = df.drop(columns=['Acoes', 'Status'])

    # Ajusta os caracteres da coluna 'Descricao'
    df['Descricao'] = ajusta_caracteres(df['Descricao'])

    # Aplica a função para criar a nova coluna 'Categoria'
    df['Categoria'] = df['Descricao'].apply(classificar_despesa)

    # Remove os caracteres 'R$', '.' e ',' da coluna 'Valor'
    df['Valor'] = df['Valor'].str.replace('R$', '')  # Remove "R$"
    df['Valor'] = df['Valor'].str.replace('.', '')  # Remove a ponto
    df['Valor'] = df['Valor'].str.replace(',', '.')  # Troca virgula por ponto
    df['Valor'] = df['Valor'].astype(float)  # Converte para float
    df = df[df['Valor'] >= 0] # Remove valores negativos

    # Remover duplicatas baseadas nos campos 'Descricao' e 'Valor'
    df = df.drop_duplicates(subset=['Descricao', 'Valor'])

    # Remove as receitas
    df = df[df['RecXDes'] != 'receita']

    # Print the DataFrame
    #print(df)

    return df

def criar_grafico(df):
    # Agrupa por categoria e soma os valores
    df_grouped = df.groupby('Categoria')['Valor'].sum()

    # Cria o gráfico de barras
    df_grouped.plot(kind='bar')

    # Define o título e os rótulos dos eixos
    plt.title('Despesas por Categoria')
    plt.xlabel('Categoria')
    plt.ylabel('Valor')
    plt.savefig('despesas_por_categoria.png')

    # Mostra o gráfico
    plt.show()

def enviar_email_mailtrap(df_grouped, total):
    sender = "Alerta Gastos <mailtrap@demomailtrap.com>"
    receiver = "Gmail Bruno <brunoropacheco@gmail.com>"

    message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

Data: {datetime.datetime.now().strftime('%d/%m/%Y')}
Despesas por Categoria:
{df_grouped}
Total: R$ {total}"""
    print(message)
    with smtplib.SMTP("live.smtp.mailtrap.io", 587) as server:
        server.starttls()
        server.login("api", os.getenv('API_MAILTRAP'))
        server.sendmail(sender, receiver, message)

def main():
    #driver = iniciar_driver()
    try:
        #html = obter_html(driver)
        #df = processar_dados_com_drive(html)
        df = processar_dados_sem_drive()
        df = ajustar_dataframe(df)
        df.to_csv('transacoes_ajustado.csv')
        #criar_grafico(df)
        df_grouped = df.groupby('Categoria')['Valor'].sum()
        enviar_email_mailtrap(df_grouped, df_grouped.sum())
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        print("acabou")
        #driver.quit()

if __name__ == "__main__":
    main()
