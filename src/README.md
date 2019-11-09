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


1. login.html

```html
{% extends 'base.html' %}

{% block content %}

    <h2>Login</h2>

    {% if error %}
        {{ error }}
    {% endif %}


    <form method="post" action="{% url 'homepage' %}">

     {% csrf_token %}

        Username:
     <input type="text" name="username"/>

        <hr>
        Password:
    <input type="password" name="password"/>
        <hr>

        <input class="btn btn-primary" type="submit" value="Login">

    </form>

{% endblock %}

```



2. Login view in accounts/views.py


```python
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth



def login(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('homepage')
        else:
            return render(request,'accounts/login.html',{'error':'wrong pass or username'})

    return render(request,'accounts/login.html',{})

```


3. 









### Creating the Product

1. Product model

```python
from django.db import models

from django.contrib.auth.models import User

class Product(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField()
    body=models.TextField()
    url=models.TextField()
    image=models.ImageField(upload_to='images/')
    icon=models.ImageField(upload_to='images/')
    votes_total=models.IntegerField(default=1)
    hunter=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
```


2. settings.py  and urls.py add media

```python


STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static'),
]


MEDIA_ROOT=os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

STATIC_ROOT=os.path.join(BASE_DIR,)
STATIC_URL = '/static/'

```


```python

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```



3. Create.html


```html

{% extends 'base.html' %}


{% block content %}
    <h1>create page</h1>

    <form method="POST" action="{% url 'create' %}" enctype="multipart/form-data">
      {% csrf_token %}

        title:
    <input type="text" name="title">
    <hr>

     body:
    <input type="text" name="body">
    <hr>
    Url
    <input type="text" name="url">
    <hr>


    <input type="file" name="icon">
    <hr>

    Image
    <input type="file" name="image">
    <hr>



        <input class="btn btn-primary" type="submit" value="create">
    </form>


{% endblock %}
```

4. Createview



```python
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone


def homepage(request):
    return render(request,'products/home.html')


@login_required
def create(request):
    if request.method=='POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product=Product()
            product.title=request.POST['title']
            product.body=request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url=request.POST['url']
            else:
                product.url='http://'+request.POST['title']
            product.icon=request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date=timezone.datetime.now()
            product.hunter=request.user
            product.save()
            return redirect('homepage')

        else:
            return render(request,'products/create.html',{'error':'Something is missing'})
    else:
        return render(request,'products/create.html')
```


---

# Products views.y

```python
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone


def homepage(request):
    products=Product.objects.all()
    return render(request,'products/home.html',{'products':products})


@login_required
def create(request):
    if request.method=='POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product=Product()
            product.title=request.POST['title']
            product.body=request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url=request.POST['url']
            else:
                product.url='http://'+request.POST['title']
            product.icon=request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date=timezone.datetime.now()
            product.hunter=request.user
            product.save()
            return redirect('/'+str(product.id))

        else:
            return render(request,'products/create.html',{'error':'Something is missing'})
    else:
        return render(request,'products/create.html')



@login_required
def detail(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    return render(request,'products/detail.html',{'product':product})



@login_required
def upvote(request,product_id):
    if request.method=='POST':
        product=get_object_or_404(Product,pk=product_id)
        product.votes_total+=1
        product.save()
        return redirect('/' + str(product.id))



```









2. home.html

```html
{% extends 'base.html' %}
{% block content %}

    {% for product in products %}

    <div class="row pt-4 pb-3">

        <div class="col-2" onclick="window.location='{% url 'detail' product.id %}';" style="cursor: pointer">
            <img src="{{ product.image.url }}" class="img-fluid">
        </div>

        <div class="col-6">
            <a href="{{ product.url }}"><h3>{{ product.title }}</h3></a>
            <p>Posted by {{ product.body|truncatewords:20 }}</p>
         </div>

        <div class="col-4">
             <a href="javascript:{document.getElementById('upvote:'{{ product.id }}).submit()}"><button class="btn btn-lg btn-primary">Upvote {{ product.votes_total }}</button></a>
        </div>

    </div>


    <form id='upvote {{ product.id }}' method="POST" action="{% url 'upvote' product.id %}">
        {% csrf_token %}
         <input type="hidden">
    </form>


    {% endfor %}


{% endblock %}
```




3. detail.html



```html
{% extends 'base.html' %}
{% block content %}

    {% for product in products %}

    <div class="row pt-4 pb-3">

        <div class="col-2" onclick="window.location='{% url 'detail' product.id %}';" style="cursor: pointer">
            <img src="{{ product.image.url }}" class="img-fluid">
        </div>

        <div class="col-6">
            <a href="{{ product.url }}"><h3>{{ product.title }}</h3></a>
            <p>Posted by {{ product.body|truncatewords:20 }}</p>
         </div>

        <div class="col-4">
             <a href="javascript:{document.getElementById('upvote:'{{ product.id }}).submit()}"><button class="btn btn-lg btn-primary">Upvote {{ product.votes_total }}</button></a>
        </div>

    </div>


    <form id='upvote {{ product.id }}' method="POST" action="{% url 'upvote' product.id %}">
        {% csrf_token %}
         <input type="hidden">
    </form>


    {% endfor %}


{% endblock %}


```
---