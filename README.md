# DDS/UnB - Assistência Estudantil

Webapp da DDS Diretoria de Desenvolvimento Social - Assistência Estudantil, Moradia universitária da UnB.

## Configurando Banco de Dados local

```
$ createdb ddsunb
$ CREATE USER projectuser WITH PASSWORD 'projectpass';
$ ALTER ROLE projectuser SET client_encoding TO 'utf8';
$ ALTER ROLE projectuser SET default_transaction_isolation TO 'read committed';
$ ALTER ROLE projectuser SET timezone TO 'UTC';
$ GRANT ALL PRIVILEGES ON DATABASE ddsunb TO projectuser;
$ \q
$ make migrate
```

## Preparando ambiente de produção

- Instalar Heroku
    - Instalar
    - heroku login
    - heroku create ddsunb
    - git push heroku master

- Criar ``__init__.py`` dentro da pasta settings decidindo qual estágio do projeto, desenvolvimento ou produção, e.g.:

```
from .prod import *
```

- Configurar o Heroku

```
$ heroku config:set DJANGO_SETTINGS_MODULE=settings.prod
$ heroku run python manage.py migrate
```
