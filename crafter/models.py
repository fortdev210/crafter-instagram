from django.db import models


class InstagramPost(models.Model):
    user_id = models.CharField(max_length=255)
    post_id = models.CharField(max_length=255)
    caption = models.TextField()
    media_type = models.CharField(max_length=255)
    media_url = models.TextField()
    
    @classmethod
    def get_posts_by_user(cls, user_id):
        return cls.objects.filter(user_id=user_id).values()
        