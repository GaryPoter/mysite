from django.urls import path

from . import views

app_name = 'devices_collect'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:d_id>/', views.detail, name='detail'),
    path('task_create/', views.analysis_task_create, name='task_create'),
    path('task_info_input/', views.analysis_task_info, name='task_info_input'),
    path('task_file_upload/', views.upload_file, name='task_file_upload_page'),
    path('do_task_file_upload/', views.do_upload_file, name='do_upload_file')
]