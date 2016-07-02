# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contador', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('cuerpo', models.TextField()),
                ('fecha', models.DateField()),
                ('hora', models.TimeField(null=True, blank=True)),
                ('imagen', models.ImageField(default=b'PrimerBiblioteca/media/poke.png', null=True, upload_to=b'PrimerBiblioteca/media', blank=True)),
                ('user', models.CharField(max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='Noti',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('cuerpo', models.TextField()),
                ('fecha', models.DateField(auto_now_add=True, null=True)),
                ('hora', models.TimeField(auto_now_add=True, null=True)),
                ('imagen', models.ImageField(default=b'PrimerBiblioteca/media/poke.png', null=True, upload_to=b'PrimerBiblioteca/media', blank=True)),
                ('user', models.CharField(max_length=24)),
            ],
        ),
    ]
