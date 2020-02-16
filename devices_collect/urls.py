from django.urls import path

from . import views

app_name = 'devices_collect'
urlpatterns = [
    path('', views.index, name='index'),
    # path('<int:d_id>/', views.detail, name='detail'),
    path('task_create/', views.analysis_task_create, name='task_create'),
    path('task_info_input/', views.analysis_task_info, name='task_info_input'),

]