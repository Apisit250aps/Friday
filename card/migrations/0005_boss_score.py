# Generated by Django 5.0 on 2023-12-13 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0004_alter_graverobinson_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='boss',
            name='score',
            field=models.IntegerField(default=1),
        ),
    ]
