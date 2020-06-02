# Trade
Django webApp to manage stocks

## Contrib

### Installing dependencies
```bash
pip install -r requirements.txt
```

### Install git hooks
```bash
pre-commit install
```

## Usage

### Local

#### Run mysql proxy to GCP DB

* trade-278014:southamerica-east1 = instance name
* tradedb: data base name

```bash
cloud_sql_proxy -instances="trade-278014:southamerica-east1:tradedb"=tcp:3306
```

#### Start app
```bash
python manage.py runserver
```

### GCP

### open in browser
* http://127.0.0.1:8000/


## Docs

* [Django webapp] - (https://docs.djangoproject.com/es/3.0/intro/tutorial01/)

## TODOS

- Manage secrets
- Google login
- Profiles
- Connect with GCP debugger
