# Generated by Django 2.2 on 2019-04-22 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20190422_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='videofile',
            field=models.FileField(null=True, upload_to='videos/', verbose_name='video'),
        ),
    ]