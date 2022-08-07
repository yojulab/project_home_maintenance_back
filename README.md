# project_home_maintenance_back

https://docs.djangoproject.com/en/4.1/intro/tutorial01/

```
% django-admin startproject webconfigs ./
```

http://127.0.0.1:8000/

https://docs.djangoproject.com/en/4.1/intro/tutorial02/

```
% python manage.py migrate
% python manage.py createsuperuser
```

```
% python -m pip install gunicorn psycopg whitenoise dj-database-url django-environ
% python -m pip freeze > requirements.txt
```

```
% heroku login
% heroku create project-home-maintenance-back
% heroku config:set secret_key='ladfa-sdfda*!-otter'
% heroku config:get secret_key -s >> .env
```

commit and push modify source to github

```
% git push heroku main
```
