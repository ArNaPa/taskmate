from todolist_app import views
from django.urls import path

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('delete/<task_id>/', views.delete_task, name='delete_task'),
    path('edit/<task_id>/', views.edit_task, name='edit_task'),
    path('alternate/<task_id>/', views.alternate_task, name='alternate_task'),
    path('todolist/', views.todolist, name='todolist'),

]
