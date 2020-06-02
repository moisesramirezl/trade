# Trade
Django webApp to manage stocks

## Pre Req

### Installing dependencies
```bash
pip install -r requirements.txt
```

### Install git hooks
```bash
pre-commit install
```

### Install SDK Cloud.
https://cloud.google.com/sdk/docs?hl=es-419


#### Installing the Cloud SQL Proxy

##### Linux 64
* wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
* chmod +x cloud_sql_proxy

##### Mac 64
* curl -o cloud_sql_proxy https://dl.google.com/cloudsql/cloud_sql_proxy.darwin.amd64
* chmod +x cloud_sql_proxy

##### Others

* go to https://cloud.google.com/python/django/appengine?hl=es-419#installingthecloudsqlproxy


## Usage

### Local

#### Run mysql proxy to GCP DB

* trade-278014:southamerica-east1 = instance name
* tradedb: data base name

```bash
cloud_sql_proxy -instances="trade-278014:southamerica-east1:tradedb"=tcp:3306
```

#### make migrations (only the first time)
```bash
python manage.py makemigrations
python manage.py makemigrations polls
python manage.py migrate
```

#### Start app
```bash
python manage.py runserver
```
#### open in browser
* http://127.0.0.1:8000/

### GCP

#### Init gcloud..

#### Deploy
```bash
gcloud app deploy
```

## Docs

* [Django webapp] - (https://docs.djangoproject.com/es/3.0/intro/tutorial01/)
* [Django + GCP] - (https://cloud.google.com/python/django/appengine?hl=es-419)

## TODOS

- Manage secrets
- Google login
- Profiles
- Connect with GCP debugger
