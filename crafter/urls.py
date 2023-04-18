from django.urls import path 
from .views import ConnectInstagram

app_name = 'instagram'

urlpatterns = [
    path('', ConnectInstagram.as_view(), name='connect_instagram')
]
