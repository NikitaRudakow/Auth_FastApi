## Installation process

To run the service locally you need to install docker

run development server MacOS:
```sh
docker compose up --build
```

install dependencies:
```sh
pip install -r requirements.txt
```

run migrations:
```sh
alembic upgrade head
```