from django.urls import path
from .views import homepage,create

urlpatterns=[
    path('',homepage,name='homepage'),
    path('create/', create, name='create'),

]