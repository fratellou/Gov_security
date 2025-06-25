from django.urls import path

from .views import department_info

app_name = 'department'

urlpatterns = [
    path('<int:department_id>/', department_info, name='department_info'),
]
