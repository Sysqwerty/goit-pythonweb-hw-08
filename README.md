# goit-pythonweb-hw-08

Make sure you have [Docker Engine](https://docs.docker.com/engine/install/) installed first

```shell
docker run --name postgres-contacts -p 5432:5432 -e POSTGRES_PASSWORD=password -d postgres
```

```shell
alembic upgrade head
```

```shell
fastapi dev main.py
```

Open in browser SWAGGER doc: [link](http://127.0.0.1:8000/docs)

To check db connection works you can use SWAGGER operation GET `/api/healthchecker`

![img.png](img.png)

All exist endpoints:

![img_1.png](img_1.png)