# Generated by Django 3.2.7 on 2021-09-23 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_user_auth_provider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='auth_provider',
        ),
    ]