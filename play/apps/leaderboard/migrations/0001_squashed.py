# Generated by Django 2.0.3 on 2019-01-21 17:28

from django.db import migrations, models
import django.db.models.deletion
import util.fields
import util.time


class Migration(migrations.Migration):

    replaces = [('leaderboard', '0001_initial'), ('leaderboard', '0002_gameleaderboard'), ('leaderboard', '0003_auto_20181016_2142'), ('leaderboard', '0004_auto_20181220_2129'), ('leaderboard', '0004_auto_20181213_0150'), ('leaderboard', '0005_merge_20181221_2129'), ('leaderboard', '0006_auto_20181221_2240'), ('leaderboard', '0007_auto_20181228_0226')]

    initial = True

    dependencies = [
        ('snake', '0001_initial'),
        ('game', '0010_merge_20181221_2129'),
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameLeaderboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', util.fields.CreatedDateTimeField(blank=True, default=util.time.now, editable=False)),
                ('modified', util.fields.ModifiedDateTimeField(blank=True, default=util.time.now, editable=False)),
                ('game', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.Game')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LeaderboardResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', util.fields.CreatedDateTimeField(blank=True, default=util.time.now, editable=False)),
                ('modified', util.fields.ModifiedDateTimeField(blank=True, default=util.time.now, editable=False)),
                ('mu_change', models.FloatField()),
                ('sigma_change', models.FloatField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Game')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserSnakeLeaderboard',
            fields=[
                ('created', util.fields.CreatedDateTimeField(blank=True, default=util.time.now, editable=False)),
                ('modified', util.fields.ModifiedDateTimeField(blank=True, default=util.time.now, editable=False)),
                ('user_snake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='snake.UserSnake')),
                ('mu', models.FloatField(null=True)),
                ('sigma', models.FloatField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='leaderboardresult',
            name='snake',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leaderboard.UserSnakeLeaderboard'),
        ),
    ]
