# Generated by Django 4.2 on 2023-04-19 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crafter', '0002_alter_instagrampost_media_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instagrampost',
            name='post_id',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
