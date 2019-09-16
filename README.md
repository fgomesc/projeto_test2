# Eventex

Sistema de Eventos encomendado pela morena.

[![Build Status](https://travis-ci.org/fgomesc/projeto_test2.svg?branch=master)](https://travis-ci.org/fgomesc/projeto_test2)

 1. clone o repositório
 2. Crie um virtualenv com python 3.5
 3. Ative o virtualenv.
 4. Instale as dependências.
 5. Configure a instância com o .env
 6. execute os testes

 ```console
git clone git@github: felipegomes/eventex.git wttd
cd wttd
python3 -m venv .wttd
source .wttd/bin/activate
pip install -r requeriments.txt
cp contrib/env-sample .env
python3 manage.py test
```
 # Como fazer Deploy

 1. Crie uma instancia no heroku.
 2. envie as configurações para o heroku.
 3. Define uma SECRET_KEY segura para a instância.
 4. Defina DEBUG=False.
 5. Configure o serviço de email.
 6. Envie o código para o heroku.


````console
heroku create minhainstancia
heroku config:push
heroku config:ser SECRET_KEY=`python3 contrib/secret_gen.py
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force
