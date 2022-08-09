
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # rest part
    path('api/v1/', include('contacts.urls')),
]
