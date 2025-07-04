from django.urls import path

from resources.views import download_resource, resources_list

urlpatterns = [
    path('resources/<int:employee_id>/',
         resources_list, name='resources_list'),
    path('download/<int:resource_id>/', download_resource,
         name='download_resource'),
]
