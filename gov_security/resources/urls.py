from django.urls import path
from .views import resources_list

urlpatterns = [
    path('resources/<int:employee_id>/', resources_list, name='resources_list'),
]
