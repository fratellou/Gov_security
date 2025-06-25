from django.urls import path
from tasks.views import tasks_list

urlpatterns = [
    path('tasks/<int:employee_id>/', tasks_list, name='tasks_list'),
]
