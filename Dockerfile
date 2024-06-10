# Use a imagem oficial do Python como base
FROM python:latest

# Instale git e cron
RUN apt-get update && apt-get install -y git cron

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Clone o repositório do GitHub
RUN git clone https://github.com/brunoropacheco/rel_finan.git .

# Instale as dependências do Python
RUN pip install --no-cache-dir -r dependencies.txt

# Copie o arquivo de crontab para o contêiner
COPY crontab /etc/cron.d/mycron

# Dê permissão para o arquivo de crontab
RUN chmod 0644 /etc/cron.d/mycron

# Aplique a crontab e inicie o cron
RUN crontab /etc/cron.d/mycron

# Comando para rodar o cron e manter o contêiner rodando
CMD ["cron", "-f"]
