from django.urls import path
from profiles.views import employee_profile

urlpatterns = [
    path('profile/<int:employee_id>/', employee_profile,
         name='employee_profile'),
]
