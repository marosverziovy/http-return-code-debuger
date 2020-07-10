# HTTP Return Code debbuger
Microapp written to tests alerts (not only) in AWS Cloduwatch.

Using env vars you can set percentual numerb of 3xx, 4xx and 5xx responses. All other reponses will be 200.

```
environment:
  HTTP_500: 3
  HTTP_400: 8
  HTTP_300: 25
```

## Run
You can run application using `docker-compose` simple as:

```
$ docker-compose up -d
```
