from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('instagram/', include('crafter.urls', namespace='crafter'))
]
