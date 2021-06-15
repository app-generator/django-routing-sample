# Django Routing Sample

Open-source sample provided by AppSeed to explain Django routing mechanism. All commands used to code the project and also the relevant updates are listed below. For newcomers, Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. 

> **For support and more [Django Samples](https://appseed.us/admin-dashboards/django) join [AppSeed](https://appseed.us).**

<br />

**Chech Python Verison**

```bash
$ python --version
Python 3.8.4 <-- All good
```

<br />

**Create/activate a virtual environment**

```bash
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
```

<br />

**Install Django**

```bash
$ pip install django
```

<br />

**Create Django Project**

```bash
$ mkdir django-sample-urls
$ cd django-sample-urls
```

Inside the new directory, we will invoke `startproject` subcomand

```bash
django-admin startproject config .
``` 

> Note: Take into account that `.` at the end of the command.

<br />

**Setup database**

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

**Start the app**

```bash
$ python manage.py runserver 
```

<br />

**Create sample app**

```bash
$ python manage.py startapp sample
```

<br />

**Add a simple route** - `sample/views.py`

```python

def hello(request): 
    return HttpResponse("Hello Django") 

```

**The browser output**

![Django Sample URLs - Simple Hello World ouput from Django.](https://user-images.githubusercontent.com/51070104/122039333-41c89e80-cddf-11eb-9a69-9e797dcb2e46.png)

<br />

**Configure Django** to use the new route

Edit `config/urls.py` as below:

```python
from django.contrib import admin
from django.urls  import path
from django.conf.urls import include, url   # <-- NEW
from sample.views import hello              # <-- NEW

urlpatterns = [
    path('admin/', admin.site.urls),
    url('', hello),                         # <-- NEW
]
```

In other words, the default route is served by `hello` method defined in `sample/views.py`

<br />

**Add dynamic content** 

Let's create a new route that shows a random number - `sample/views.py`.

```python
...
from random import random
...
def myrandom(request): 
    return HttpResponse("Random - " + str( random() ) ) 

```

The new medthod invoke `random()` from Python core library, convert the result to a string and return the result. 

**The browser output**

![Django Sample URLs - Display random number from Django.](https://user-images.githubusercontent.com/51070104/122039552-789eb480-cddf-11eb-9f01-8707c19ded69.png)

<br />

**Display a random image**

The controller code can be found in `sample/views.py`.

```python
...
import requests
...
def randomimage(request):
    r = requests.get('http://thecatapi.com/api/images/get?format=src&type=png')
    return HttpResponse( r.content, content_type="image/png")
```

To see the effects in the browser, the routing should be updated acordingly. 

```python
# Contents of config/urls.py
...
from sample.views import hello, myrandom, randomimage # <-- Updated 
...
urlpatterns = [
    path('admin/'     , admin.site.urls),
    url('randomimage' , randomimage),                 # <-- New
    url('random'      , myrandom),
    url(''            , hello), 
]
```

**The browser output**

![Django Sample URLs - Display random image from Django.](https://user-images.githubusercontent.com/51070104/122039724-a1bf4500-cddf-11eb-8dc5-d8171284bf4a.png)

<br />

---
Django Routing - Open-source Sample provided by [AppSeed](https://appseed.us/app-generator). 
