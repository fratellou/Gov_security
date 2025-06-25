from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('profiles/', include('profiles.urls')),
    path('departments/', include('departments.urls')),
    path('tasks/', include('tasks.urls')),
    path('resources/', include('resources.urls')),
    path('home/', include('home.urls')),
    path('', RedirectView.as_view(url='/accounts/login/', permanent=True)),
]

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
