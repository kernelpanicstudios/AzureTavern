# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=200)),
                ('short_name', models.CharField(max_length=60)),
                ('gender', models.CharField(blank=True, max_length=3, choices=[(b'm', 'Male'), (b'f', 'Female')])),
                ('description', models.CharField(max_length=500)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('player', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'modified_date',
                'verbose_name': 'character',
                'verbose_name_plural': 'characters',
            },
        ),
        migrations.CreateModel(
            name='CharacterNote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, blank=True)),
                ('text', models.CharField(max_length=4000)),
                ('permissions', models.CharField(max_length=3, choices=[(b'pr', 'Private'), (b'li', 'Limited'), (b'pu', 'Public')])),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('character', models.ForeignKey(to='rptavern.Character')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80)),
                ('subtitle', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('gm', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GamePlayer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('game', models.ForeignKey(to='rptavern.Game')),
                ('player', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='players',
            field=models.ManyToManyField(related_name='players', through='rptavern.GamePlayer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterOrderWithRespectTo(
            name='characternote',
            order_with_respect_to='character',
        ),
        migrations.AlterUniqueTogether(
            name='character',
            unique_together=set([('player', 'full_name')]),
        ),
    ]
