# Generated by Django 3.2 on 2021-10-04 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20211003_2031'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='customuser',
            name='user_search_gin',
        ),
    ]
