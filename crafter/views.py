import requests

from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse

from .models import InstagramPost


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
        user_id = data['user_id']
        access_token = data['access_token']

        # add access_token and user_id to request session
        request.session['access_token'] = access_token
        request.session['user_id'] = user_id

        api_url = f'https://graph.instagram.com/{user_id}/media'

        # Set the API parameters
        params = {
            'fields': 'id,media_type,media_url,caption,permalink',
            'access_token': access_token,
            'limit': 10
        }

        # Send a GET request to the API endpoint
        response = requests.get(api_url, params=params)

        # Parse the JSON response
        json_response = response.json()

        # Extract the list of posts
        posts = json_response['data']

        # Loop through the posts and print their captions and permalinks
        for post in posts:
            # Create an InstagramPost object with the retrieved data
            post['user_id'] = user_id
            InstagramPost.save_post(post)
        return redirect(reverse('crafter:show_posts'))
    return redirect(reverse('crafter:connect_instagram'))


def show_posts(request):
    if request.access_token:
        user_id = request.user_id
        posts = InstagramPost.get_posts_by_user(user_id)

        return render(request, 'posts.html', {'posts': posts})
    else:
        return redirect(reverse('crafter:connect_instagram'))
