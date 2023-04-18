from django.urls import path 
from django.views.generic import TemplateView
from .views import connect_instagram, exchange_code_token

app_name = 'crafter'

urlpatterns = [
   path('', connect_instagram, name='connect_instagram'),
   path('exchange-token',exchange_code_token, name='exchange-token'), 
]