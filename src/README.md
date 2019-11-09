# Producthunt



### Part 1 Signup

1. accounts urls.py

```python
from django.urls import path
from . import views



urlpatterns=[
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
]
```

2. producthunt src urls.py


```python

from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('products.urls')),
    path('accounts/',include('accounts.urls')),
]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

```



3. Accounts/signup.html

```html
{% extends 'base.html' %}

{% block content %}

    <h2>Sign Up</h2>

    {% if error %}
        {{ error }}
    {% endif %}


    <form method="post" action="{% url 'signup' %}">

     {% csrf_token %}

        Username:
     <input type="text" name="username"/>

        <hr>
        Password:
    <input type="password" name="password1">
        <hr>
        Confirm Password:
    <input type="password" name="password2">

        <input class="btn btn-primary" type="submit" value="Sign Up">

    </form>

{% endblock %}

```



4. base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>

    {% load staticfiles %}

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width">
    <title>Title</title>

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>

    <header>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
          <div class="container">
            <a class="navbar-brand" href="{% url 'homepage' %}">
              <img src="{% static 'medium.png'%}" alt="Loto" class="d-inline-block align-top"></a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div class="navbar-nav ml-auto">
                    <a class="nav-item nav-link" href="{% url 'signup' %}">Sign Up</a>
                    <a class="nav-item nav-link" href="{%  url 'login' %}">Login</a>
                </div>
            </div>
        </div>
        </nav>
    </header>



<div class="container">
 {% block content %}


 {% endblock %}
</div>

    <footer class="text-muted">
        <div class="container text-center">
            <p>@ Loto copyright</p>
        </div>
    </footer>



<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

</body>
</html>
```




### Login

