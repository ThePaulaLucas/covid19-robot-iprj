# Generated by Django 3.0.5 on 2020-05-28 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='novidade',
            name='subject',
            field=models.TextField(blank=True),
        ),
    ]
