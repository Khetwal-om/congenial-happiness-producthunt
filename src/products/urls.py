from django.urls import path
from .views import homepage,create,detail,upvote

urlpatterns=[
    path('',homepage,name='homepage'),
    path('create/', create, name='create'),
    path('<int:product_id>',detail,name='detail'),
    path('<int:product_id>/upvote', upvote, name='upvote'),

]