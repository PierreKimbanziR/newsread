from django.contrib import admin
from django.urls import path
from newspages import views

urlpatterns = [
    path("bbc/", views.Bbc, name="bbc-news"),
    path("abc/", views.Abc_News, name="abc_news"),
    path("ap/", views.AP, name="ap")
]
