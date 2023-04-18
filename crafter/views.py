import requests
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    user = request.user
    try:
        account = SocialAccount.objects.get(user=user, provider='instagram')
    except SocialAccount.DoesNotExist:
        account = None

    posts = []
    if account:
        access_token = account.socialtoken_set.first().token
        response = requests.get(
            f'https://graph.instagram.com/me/media?fields=id,caption,media_url,thumbnail_url,permalink,timestamp,username&access_token={access_token}'
        )
        if response.ok:
            data = response.json()
            for post in data['data']:
                posts.append({
                    'id': post['id'],
                    'caption': post['caption'],
                    'image_url': post['media_url'],
                    'likes': 0,  # You can fetch the number of likes using the Instagram Graph API
                })

    return render(request, 'home.html', {'user': user, 'posts': posts})
