from django.urls import path
from home.views import home_view, logout_view, post_message


urlpatterns = [
    path('', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('post_message/', post_message, name='post_message'),
]
