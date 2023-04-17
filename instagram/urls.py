from django.urls import path 
from .views import connect_instagram

app_name = 'instagram'

urlpatterns = [
    path('connect', connect_instagram, name='connect_instagram')
]
