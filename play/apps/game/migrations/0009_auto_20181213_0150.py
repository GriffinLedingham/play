# Generated by Django 2.0.3 on 2018-12-13 01:50

from django.db import migrations
import util.fields
import util.time


class Migration(migrations.Migration):

    dependencies = [("game", "0008_remove_game_snake_uniqueness")]

    operations = [
        migrations.AddField(
            model_name="gamesnake",
            name="created",
            field=util.fields.CreatedDateTimeField(
                blank=True, default=util.time.now, editable=False
            ),
        ),
        migrations.AddField(
            model_name="gamesnake",
            name="modified",
            field=util.fields.ModifiedDateTimeField(
                blank=True, default=util.time.now, editable=False
            ),
        ),
    ]
