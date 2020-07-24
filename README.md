# GITHUB API CONSUMER
 Programa em python feito para praticar consumo de informações providas de api de terceiros.

# Bibliotecas utilizadas:
- import requests
- from requests.auth import HTTPBasicAuth
- import sys
- import json

# Sintaxe:
Para puxar informações de só um usuário:
```sh# 
python .\using_git_api.py <username> 
````
Para puxar informações de vários usuários (parte ainda não implementada)
```sh#
python .\using_git_api.py
````
# Detalhes de estudos
Um ponto interessante ao trabalhar com a api do git é que há limitações a serem trabalhadas, como por exemplo a limitação de resultados sem autenticação prévia que o força a ir atrás deste tipo de informação caso não saiba pra que server autenticação e cookies, acaba sendo muito positivo. Outro ponto posítivo é pensar o que dá pra fazer com todas as informações que podem ser reunidas, afinal de contas informação é poder.git