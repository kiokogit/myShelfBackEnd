# Generated by Django 3.2.7 on 2022-02-23 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0009_quote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='author',
            new_name='source',
        ),
    ]
