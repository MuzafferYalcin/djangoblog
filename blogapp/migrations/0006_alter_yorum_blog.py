# Generated by Django 4.2.2 on 2023-08-01 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_yorum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yorum',
            name='Blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogapp.blog'),
        ),
    ]