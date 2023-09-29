# DJANGO FRAMEWORK

## Creating and build a django project and app 
For development: create a python virtual environment, in this case `pipenv`

- in the intended project folder go `pipenv install django` to start the environment and the framework to install
- `pipenv shell` to launch to the virtual environment shell

To install django if using other or not using virtual environment: `pip install django` 

To initialize the project `django-admin startproject <projectname> .`

To launch/build the app `python manage.py runserver`

To create a new module (or app) `python manage.py startapp <new-app-name>`

To make the app available go to the original app create after start the project `setting.py` find `INSTALLED_APPS` and add the app name to the list 
## Project structure
Shell command:
```shell
django-admin startproject myserver .
python manage.py startapp myapp
```
The project should be like this
```
project-root
- myserver
--- __pycache__
--- __init__.py
--- asgi.py
--- urls.py
--- wsgi.py

- myapp
--- migrations
--- admin.py
--- models.py
--- test.py
--- views.py

- manage.py
```

## Creating endpoint
To create a endpoint we need:
- a controller (or views) in `views.py`, this is where the logics of the url end point will be define. It's can be a function base or a class base 

- a urls definitions in `urls.py` to defined the end point and which view that endpoint will perform 
```python 
from django.urls import path
from . import views

urlpatterns = [
    #function base class view
    path('<int:id>/', views.myview(), name='question'),
    #class base view
    path("", views.MyView.as_view(), name='index')
]
```
- referencing the application endpoints to the project in the main app `urls.py`




### views.py 
each endpoint will alway have a views to serve the product
Both frontend and backend routing have a function base and class base view
- all function base and class base have a same prototype: receiving a request as argument and return HttpResponse
- in function base, method identification is required to know which request method are available and which method will perform what
- in class base, each method `get()`,`post()`,`put()`, `delete()`, etc, will tell the system how which method will do, which are available. 
- Django also provide some views that only need to inherited to quickly implement some common task

```python
#function base
def myview(request, *args, **kwargs):
    #logics here
    return HttpResponse()

#class base
class MyView(django.views.generic.View):
    def get(request, *args, **kwargs): # GET method
        #logics here
        return HttpResponse()
```

### urls.py
routing definition is in a `urlpatterns` list which contain the `path(<your route pattern>, <your view reference>)`

for referencing the app routing int the main app add `path(<prefered route for the app>, include(<your app>.urls))` to the `urls.py`'s `urlpatterns`
```python
from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include(myapp.urls)), 
]
```

## Endpoint logic and database interaction
End point logic will alway implemented in views function or class

To easily implement a rest api endpoints, install `djangorestframework` using `pip`
and add the app to `setting.py`

### Models and Database interaction 
For interacting with MySQL specifically install `mysqlclient` 

In the main app `setting.py` provide the database information to the system in `DATABASE` list, example for mysql:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "my_db_name"
        'USER': "my_username",
        'PASSWORD': "my_password",
        'HOST': "db_server_host",
        'PORT': "db_server_port",
    }
}
``` 
To interact with the database, django provided a ORM for defining the database schema and querying data
- All models can be define in `models.py` 
- Each models will have a Model Managers default to `objects` to performing query

### Backend with `djangorestframework`
For serializing models to Json format, `djangorestframework` provide a set of `serializes` models for both validating and serialize/deserialize the data model 

Access the request's body using `request.data`, the framework will automatically parsing the content in to python dict

The framework provided a Object to automatically serve json format when accessing end point using `Response()`

**Adding Authentication logic** 
- `djangorestframework` class base view provide a properties for defining with build in authentication method the endpoint will use
- To create a custom authentication method, implement it using a new class inherited from `BaseAuthentication` and implement the authentication method

### Frontend with Django template
Django provide a template system to create a better data representation for the html web page

The template support logic base rendering, render out the data using template context, and support inherited template 

Django also provide static file serving and can access it with template and static file location definition

All template will have a `.html` extension and stored in `templates` folder created by user

To serving the template, the view class method or function must return a `render(<html template>, <context dictionary>)` 

## Application deployment
Before serving the project in production
- Update the database information to the current production database
- Disable DEBUG mode in the main application `setting.py` > `DEBUG=False`
- Creating a project dependency file: `pip freeze > requirements.txt` in the shell

In the production deployment
- Make sure `python` and `pip` are available
- Install project dependency `pip install -r requirements.txt --no-cache-dir`
- start building and run the project by command `python manage.py runserver 0.0.0.0:<prefered-port> --noreload`

If the system database is brand new or after the models in the application has some changes, go to project shell and perform a migration 
```shell
python manage.py makemigrations
python manage.py migrate
``` 
## Reference

### Documentation
https://docs.djangoproject.com/en/4.2/

https://django-rest-framework.org/

### Tutorial
https://www.youtube.com/watch?v=rHux0gMZ3Eg

https://www.youtube.com/watch?v=c708Nf0cHrs

https://www.youtube.com/watch?v=t10QcFx7d5k&t=2957s

https://www.youtube.com/watch?v=F5mRW0jo-U4&t=12667s