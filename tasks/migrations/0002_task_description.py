# Generated by Django 3.1.3 on 2020-11-22 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.CharField(default='', max_length=500),
        ),
    ]
