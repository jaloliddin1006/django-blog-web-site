from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('article/<int:id>/detail/', article_detail, name="article_detail"),
    path('article/<int:id>/update/', article_update, name="article_update"),
    path('article/<int:id>/delete/', article_delete, name="article_delete"),
    path('article/create/', article_create, name="article_create"),
]