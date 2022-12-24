from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from dexter import views

urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),
]