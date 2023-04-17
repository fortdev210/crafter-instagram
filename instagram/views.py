from django.shortcuts import render


def connect_instagram(request):
  return render(request, 'instagram/connect.html')



