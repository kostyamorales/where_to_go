from django.contrib import admin
from django.urls import path
from places import views


urlpatterns = [
    path('<int:id>/', views.show_place_page)
]