# Generated by Django 3.1.1 on 2020-12-15 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20201206_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suggestionmodel',
            name='author',
        ),
    ]
