# Generated by Django 3.2.7 on 2022-02-22 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0006_alter_diary_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
