from django.contrib import admin
from django.urls import path, include

api_prefix = 'api/v4/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(api_prefix, include('navigation.urls')),
    path(api_prefix, include('benefits.urls')),
]
