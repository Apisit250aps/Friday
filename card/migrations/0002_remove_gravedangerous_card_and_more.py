# Generated by Django 5.0 on 2023-12-11 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gravedangerous',
            name='card',
        ),
        migrations.RemoveField(
            model_name='gravedangerous',
            name='game',
        ),
        migrations.AlterField(
            model_name='robinson',
            name='active',
            field=models.IntegerField(choices=[(0, 'none'), (1, 'health + 1'), (2, 'health + 2'), (3, 'card + 1'), (4, 'card + 2'), (5, 'destroy'), (6, 'double'), (7, 'copy'), (8, 'phase'), (9, 'sort'), (10, 'swap 1'), (11, 'swaps 2'), (12, 'under'), (-1, 'max = 0'), (-2, 'health - 1'), (-3, 'health - 2'), (-4, 'stop')]),
        ),
        migrations.DeleteModel(
            name='deckDangerous',
        ),
        migrations.DeleteModel(
            name='graveDangerous',
        ),
    ]
