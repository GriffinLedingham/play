# Generated by Django 2.0.3 on 2018-09-12 04:03

from django.db import migrations

from util.fields import ShortUUIDField

def generate_ids(apps, schema_editor):
    GameSnake = apps.get_model('game', 'GameSnake')
    for gs in GameSnake.objects.all():
        gs.id = ShortUUIDField.generate_short_uuid(prefix='gs')
        gs.save(update_fields=['id'])


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_adds_id_column_to_game_snake'),
    ]

    operations = [
        migrations.RunPython(generate_ids)
    ]