# Generated by Django 4.2.2 on 2023-08-02 08:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogapp', '0006_alter_yorum_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='sevilenler',
            field=models.ManyToManyField(related_name='selenler', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blog',
            name='sevilmeyenler',
            field=models.ManyToManyField(related_name='sevilmeyenler', to=settings.AUTH_USER_MODEL),
        ),
    ]
