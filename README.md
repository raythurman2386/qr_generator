# Flask QR Code Generator

This is designed to be a free qr code generator with basic authentication

Styled utilizing Bootstrap

`cd qr_generator`

I use virtual environments for all of my python projects, to create a venv inside of the project before installing deps, run:
Virtualenv will need to be installed on your machine as well as obviously Python 3

`python -m venv venv`

`pip install -r requirements.txt`

Initialize SQLite DB

`flask db init`

Migrate SQLite DB

`flask db migrate`

Upgrate DB

`flask db upgrade`


Application utilizes the following ENV vars

```
SECRET_KEY
APP_SETTINGS
DATABASE_URL
FLASK_APP
FLASK_DEBUG
```

APP_SETTINGS tells the app which config to use for dev, testing, production

Once all env vars are filled in and deps installed, app can be started with:

`python manage.py run`

App can be tested by running:

`python manage.py test`

Admin can be created for the application by running:

`python manage.py create_admin`