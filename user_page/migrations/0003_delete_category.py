# Generated by Django 4.0.3 on 2022-05-28 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0002_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
