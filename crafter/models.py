from django.db import IntegrityError, models


class InstagramPost(models.Model):
    user_id = models.CharField(max_length=255)
    post_id = models.CharField(max_length=255, unique=True)
    caption = models.TextField()
    media_type = models.CharField(max_length=255)
    media_url = models.TextField()

    @classmethod
    def get_posts_by_user(cls, user_id):
        return cls.objects.filter(user_id=user_id).values()

    @classmethod
    def save_post(cls, post_data):
        try:
            instagram_post = cls(
                user_id=post_data['user_id'],
                post_id=post_data['post_id'],
                caption=post_data['caption'],
                media_type=post_data['media_type'],
                media_url=post_data['media_url']
            )
            instagram_post.save()
        except IntegrityError:
            # Handle if the post with the same post_id already exists
            pass
