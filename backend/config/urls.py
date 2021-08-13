from django.contrib import admin
from django.urls import path, include
from django.conf import settings


api_patterns = [
    path('auth/', include('rest_framework.urls')),
    path('sites/', include('apps.sites.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_patterns)),
]