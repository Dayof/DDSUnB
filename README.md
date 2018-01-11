# DDS/UnB - Assistência Estudantil

Webapp da DDS Diretoria de Desenvolvimento Social - Assistência Estudantil, Moradia universitária da UnB.

## Preparando ambiente de produção


- LOCAL : Criar ``__init__.py`` dentro da pasta settings decidindo qual estágio do projeto, desenvolvimento ou produção, e.g.:

```
from .dev import *
```

- HEROKU (necessário Heroku instalado na máquina):

```
heroku config:set DJANGO_SETTINGS_MODULE=settings.prod
```
