from django.urls import path
from .views import *

urlpatterns = [
    path('posts', listar_posts, name='posts')
]