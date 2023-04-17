from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount


def connect_instagram(request):
  # instagram_account = SocialAccount.objects.filter(user=request.user, provider='instagram').first()
  # context = {
  #   'instagram_account': instagram_account
  # }
  return render(request, 'crafter/connect.html')
  
