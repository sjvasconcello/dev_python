# Django Avanzado

## Video 6 - Codebase:Docker
Listar contenedores
```bash
$ docker-compose -f local.yml ps
```


Pro Tip
```bash
$ export COMPOSE_FILE=local.yml
$ docker-compose build
$ docker-compose up
$ docker-compose ps
$ docker-compose down
```

Comandos de administración
```bash
$ docker-compose -f local.yml run --rm django 
    \ python manage.py createsuperuser
# Exportando COMPOSE_FILE
$ docker-compose run --rm django COMMAND
$ docker-compose run -- django \
    python manage.py createsuperuser
```

Habilitar debugger
```bash
$ docker-compose up
$ docker-compose pd
$ docker rm -f <ID>

$ docker-compose run --rm --service-ports django
```

Recordar
```bash
$ docker container
$ docker images
$ docker volume
$ docker network
$ ls rm prune -a -q
```

Listar contenedores
```bash
```

