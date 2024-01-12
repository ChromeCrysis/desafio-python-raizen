# Desafio entrevista Python 

Este projeto é um desafio para a vaga de desenvolvedor Python, consiste em uma API feita utilizando o framework Flask que consome a API do openweather para buscar a previsão dos próximos 5 dias.

## Tecnologias de desenvolvimento utilizadas

- Python
- Flask
- MongoDB
- Pymongo

## Objetivos

O objetivo do projeto é a criação de uma API REST que faz a busca da previsão do tempo para os próximos 5 dias na API do openweather, e, guarda os resultados em um banco de dados MongoDB para futura visualização.

## Endpoints
### Weather
- GET - weather/<city> . Busca o clima em uma cidade especifica passada por parâmetro na URL e salva em um banco de dados mongoDB.
- GET - weather/history . Busca no banco de dados o historico de pesquisas.
- GET - weather/history/<city> . Busca no bando de dados o clima de uma cidade especifica passada por parâmetro na URL.

## Instruções de uso
Para rodar o projeto faça o download desse repositório utilizando o comando ``git clone https://github.com/ChromeCrysis/desafio-python-raizen.git`` 

Para instalar as dependências execute o comando ``pip install -r requirements.txt``.
