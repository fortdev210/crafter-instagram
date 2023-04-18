from django.contrib import admin
from .models import InstagramPost

@admin.register(InstagramPost)
class InstagramPostAdmin(admin.ModelAdmin):
  list_display = ('user_id', 'post_id', 'caption', 'media_type', 'media_url')
  

