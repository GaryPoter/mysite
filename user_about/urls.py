from django.urls import path

from . import views

app_name = 'user_about'
urlpatterns = [
    path('login/', views.login, name='index'),
    path('do_login/', views.do_login, name='do_login')
]