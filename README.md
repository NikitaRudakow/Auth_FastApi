## Installation process

To run the service locally you need to install docker

run development server MacOS:

```sh
docker compose up -d --build
```

run migrations:
```sh
docker-compose exec app bash
```

```sh
alembic upgrade head
```

run tests

```sh
docker compose -f docker-compose.test.yml run --rm app pytest -s
```
