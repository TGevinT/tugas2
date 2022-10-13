from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user, create_task, update_task, delete_task,show_json, add_task_ajax
from todolist.views import delete_task_ajax, update_task_ajax

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('update-task/<int:id>', update_task, name='update_task'),
    path('delete-task/<int:id>', delete_task, name='delete_task'),
    path('json/', show_json, name="show_json"),
    path('add_task_ajax/', add_task_ajax, name='add_task_ajax'),
    path('update_task_ajax/<int:id>', update_task_ajax, name='update_task_ajax'),
    path('delete_task_ajax/<int:id>', delete_task_ajax, name='delete_task_ajax')
]