# README.md

## Descrição

ChatBot não conversacional criado em Python que recebe e processa alertas dos Sensores Meraki e publica os alertas como mensagens no Webex Teams. Uma vez processado o alerta é anexado a mensagem um snapshot da Câmera Meraki associada ao sensor que emitiu o alerta no grupo __[MERAKI EXP] Sensores__.

## Instalação

Clone o repositório
```bash
git clone https://github.com/CIL-Rio/meraki-alert-chatbot.git
```
Navegue até o diretório do projeto
```
cd meraki-alert-chatbot
```
Instale as dependências usando pip
```bash
pip install -r requirements.txt
```
Renomeie o arquivo `./src/app/env-example` para `./src/app/.env` e adicione suas informações no arquivo `.env`
   ```env
   WEBEX_TOKEN=seu_token_webex
   WEBEX_URI=sua_uri_webex
   MERAKI_TOKEN=seu_token_meraki
   ROOM_ID=id_da_sala
```
Execute o arquivo principal usando python
```bash
python __main__.py
```

## Como usar

O Bot é um servidor web que responde as mensagens recebidas da Meraki via webhook. O Webhook um único endpoint '/', que aceita solicitações POST e GET.

- Para as solicitações POST, o endpoint espera um corpo de solicitação JSON contendo informações de alerta. Se o alerta já foi processado anteriormente, ele retorna um status OK sem fazer nada. Caso contrário, ele publica uma mensagem no Webex Teams contendo informações sobre o alerta, faz o download do Snapshot da Câmera associada ao sensor no momento do alerta e publica a imagem em espaço do Webex Teams.

- Para as solicitações GET, o endpoint simplesmente retorna a string 'Hello World!' e um status OK.

## Contribuindo

Se você quiser contribuir com este projeto, por favor, faça um fork do repositório e submeta um Pull Request com suas alterações.

## Licença

Este projeto é licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter detalhes.