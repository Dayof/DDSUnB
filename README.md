# DDS/UnB - Assistência Estudantil

Webapp da DDS Diretoria de Desenvolvimento Social - Assistência Estudantil, Moradia universitária da UnB.

## Preparando ambiente de desenvolvimento

### Instalação

```
$ make installd
```

### Virutalenv

- Iniciar ambiente virtual
- Iniciar variáveis locais no arquivo ``$VIRTUAL_ENV/bin/postactivate``
    - DATABASE_USER
    - DATABASE_PASSWORD

```
$ source venv/bin/activate
$ source venv/bin/postactivate
```

### Configurando Banco de Dados Local

```
$ createdb ddsunb
$ CREATE USER databaseuser WITH PASSWORD 'databasepassword';
$ ALTER ROLE databaseuser SET client_encoding TO 'utf8';
$ ALTER ROLE databaseuser SET default_transaction_isolation TO 'read committed';
$ ALTER ROLE databaseuser SET timezone TO 'UTC';
$ GRANT ALL PRIVILEGES ON DATABASE ddsunb TO databaseuser;
$ GRANT ALL ON ALL TABLES IN SCHEMA public to databaseuser;
$ GRANT ALL ON ALL SEQUENCES IN SCHEMA public to databaseuser;
$ GRANT ALL ON ALL FUNCTIONS IN SCHEMA public to databaseuser;
$ \q
$ make migrate
```

## Preparando ambiente de produção

- Heroku
    - Instalar
    - heroku login
    - heroku create ddsunb
    - git push heroku master

<!-- - Criar ``__init__.py`` dentro da pasta settings decidindo qual estágio do projeto, desenvolvimento ou produção, e.g.:

```
from .prod import *
``` -->
<!--
- Configurar o Heroku

```
$ heroku config:set DJANGO_SETTINGS_MODULE=settings.prod
$ heroku run python manage.py migrate
``` -->
