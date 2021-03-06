# Generated by Django 2.2 on 2019-04-22 16:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_auto_20190422_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=1000, null=True, verbose_name='Yorum')),
                ('comment_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('blog', models.ForeignKey(null=True, on_delete=True, related_name='comment', to='posts.Post')),
                ('user', models.ForeignKey(default=1, null=True, on_delete=True, related_name='comment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Yorumlar',
            },
        ),
    ]
