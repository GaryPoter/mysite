from django.urls import path

from . import views

app_name = 'devices_collect'
urlpatterns = [
    path('login/', views.login, name='index'),
]