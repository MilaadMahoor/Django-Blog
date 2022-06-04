from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "articles"
urlpatterns = [
    path('', views.article_list, name = "list"),
    path('create',views.create_Article, name = "create"),
    path('<title>',views.article_detail, name = "detail"),


]
