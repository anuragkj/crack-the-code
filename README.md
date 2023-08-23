# Crack the code

This is a web server that can host quizzes.

## Usage

### Install dependencies

```bash
pip install -r requirements.txt
```

### Fix Conf URL Path
In the virtual env: \venv\lib\site-packages\markdownx\urls.py

Replace:

```bash
from django.conf.urls import url
```

With:

```bash
from django.urls import re_path as url
```

### Make migrations

```bash
python manage.py makemigrations
```

### Perform migration

```bash
python manage.py migrate
```

### Create a super user

```bash
python manage.py createsuperuser
```

### Run server

```bash
python manage.py runserver 
```
