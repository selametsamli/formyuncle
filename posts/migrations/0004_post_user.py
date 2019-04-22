# Generated by Django 2.2 on 2019-04-22 18:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=True, related_name='blog', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
