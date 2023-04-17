from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crafter/', include('crafter.urls', namespace='crafter')),
    path('accounts/', include('allauth.urls'))
]
