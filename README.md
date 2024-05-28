# Coleta e Processamento de Dados de Transações do Mobills

Este programa Python coleta dados de transações do site Mobills, processa os dados para classificá-los e limpá-los, e em seguida gera um relatório resumido. O programa também pode enviar um e-mail com os dados processados.

## Pré-requisitos

- Python 3.x
- Google Chrome
- Uma conta Google
- Uma conta no Mobills
- Variáveis de ambiente configuradas para suas credenciais do Gmail (`EMAIL_GMAIL`, `SENHA_GMAIL`) e chave de API do Mailtrap (`API_MAILTRAP`)

## Instalação

1. Clone este repositório:
    ```sh
    git clone https://github.com/seunomeusuario/seurepositorio.git
    cd seurepositorio
    ```

2. Instale os pacotes Python necessários:
    ```sh
    pip install -r requirements.txt
    ```

3. Certifique-se de que você tem o Google Chrome instalado.

4. Configure as variáveis de ambiente para suas credenciais do Gmail e chave de API do Mailtrap:
    ```sh
    export EMAIL_GMAIL='seu_email_gmail'
    export SENHA_GMAIL='sua_senha_gmail'
    export API_MAILTRAP='sua_chave_api_mailtrap'
    ```

## Uso

### Funções

- `ajusta_caracteres(coluna)`: Normaliza caracteres especiais nas colunas de texto.
- `classificar_despesa(descricao)`: Classifica despesas com base em palavras-chave específicas.
- `iniciar_driver()`: Inicializa o driver Chrome do Selenium.
- `obter_html(driver)`: Faz login no Mobills, navega até a página de transações e recupera o HTML da página.
- `processar_dados_sem_drive()`: Processa dados de transações a partir de um arquivo HTML salvo anteriormente.
- `processar_dados_com_drive(html)`: Processa dados de transações diretamente a partir do conteúdo HTML.
- `ajustar_dataframe(df)`: Limpa e prepara o DataFrame para análise.
- `criar_grafico(df)`: (Opcional) Cria um gráfico de barras das despesas por categoria.
- `enviar_email_mailtrap(df_grouped, total)`: Envia um e-mail com os dados processados usando o Mailtrap.

### Executando o Script

1. Para executar o script, use o seguinte comando:
    ```sh
    python main.py
    ```

2. O script executará os seguintes passos:
    - Inicializa o driver do Selenium.
    - Faz login no Mobills usando sua conta do Gmail.
    - Recupera e processa os dados de transações.
    - Ajusta e limpa o DataFrame.
    - (Opcional) Cria um gráfico de barras das despesas por categoria.
    - Envia um e-mail com o resumo das despesas.

3. O script salvará os dados processados em `transacoes_ajustado.csv`.

## Notas

- Certifique-se de que as variáveis de ambiente para as credenciais do Gmail e chave de API do Mailtrap estão corretamente configuradas antes de executar o script.
- O script utiliza `undetected-chromedriver` para contornar a detecção de bots.
- A função opcional de criação de gráfico (`criar_grafico()`) está comentada, mas pode ser habilitada se necessário.

## Solução de Problemas

- Se você encontrar problemas ao fazer login no Mobills, verifique se suas credenciais do Gmail estão corretas e se você tem uma conexão estável à internet.
- Se o script não encontrar certos elementos HTML, verifique se houve alterações no layout do site Mobills.

## Licença

Este projeto é licenciado sob a Licença MIT.

---

Sinta-se à vontade para entrar em contato caso tenha dúvidas ou encontre problemas!

---

**Autor**: Bruno Rodrigues Pacheco

**Contato**: brunoropacheco@gmail.com

---

