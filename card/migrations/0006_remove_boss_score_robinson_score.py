# Generated by Django 5.0 on 2023-12-13 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0005_boss_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boss',
            name='score',
        ),
        migrations.AddField(
            model_name='robinson',
            name='score',
            field=models.IntegerField(default=1),
        ),
    ]