# Django Sample URLs

Open-source sample provided by AppSeed to explain Django routing mechanism. All commands used to code the project and also the relevant updates are listed below. 

> For support and more samples join [AppSeed](https://appseed.us).

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

<br />

---
Django Sample URLs - Open-source Django sample provided by AppSeed [App Generator](https://appseed.us/app-generator) 
