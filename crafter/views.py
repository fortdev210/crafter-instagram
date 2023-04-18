from django.http import HttpResponse
import requests
# from allauth.socialaccount.models import SocialAccount
# from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings

# @login_required
# def home(request):
#     user = request.user
#     try:
#         account = SocialAccount.objects.get(user=user, provider='instagram')
#     except SocialAccount.DoesNotExist:
#         account = None

#     posts = []
#     if account:
#         access_token = account.socialtoken_set.first().token
#         response = requests.get(
#             f'https://graph.instagram.com/me/media?fields=id,caption,media_url,thumbnail_url,permalink,timestamp,username&access_token={access_token}'
#         )
#         if response.ok:
#             data = response.json()
#             for post in data['data']:
#                 posts.append({
#                     'id': post['id'],
#                     'caption': post['caption'],
#                     'image_url': post['media_url'],
#                     'likes': 0,  # You can fetch the number of likes using the Instagram Graph API
#                 })

#     return render(request, 'home.html', {'user': user, 'posts': posts})


def connect_instagram(request):
    oauth_url = f"https://api.instagram.com/oauth/authorize?client_id={settings.INSTAGRAM_APP_ID}&scope=user_profile,user_media&response_type=code&redirect_uri={settings.INSTAGRAM_REDIRECT_URI}"
    return render(request, 'connect.html', {'url': oauth_url})

def exchange_code_token(request):
    code = request.GET.get('code')
    url = 'https://api.instagram.com/oauth/access_token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'client_id': settings.INSTAGRAM_APP_ID,
        'client_secret': settings.INSTAGRAM_APP_SECRET,
        'grant_type': 'authorization_code',
        'redirect_uri': settings.INSTAGRAM_REDIRECT_URI,
        'code': code
    }
    response = requests.post(url, headers=headers, data=data)
    
    if response.ok:
        data = response.json()
        print("access token ", data)
    
    return HttpResponse('OK')
    