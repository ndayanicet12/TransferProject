# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-02 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfers', '0002_auto_20170531_0847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfert',
            name='tarif',
        ),
        migrations.AlterField(
            model_name='transfert',
            name='cin',
            field=models.CharField(max_length=50, verbose_name="Carte nationale d'identite"),
        ),
        migrations.AlterField(
            model_name='transfert',
            name='datedepot',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date du  depot'),
        ),
        migrations.AlterField(
            model_name='transfert',
            name='first_namesender',
            field=models.CharField(max_length=30, verbose_name="Prenom de l' expediteur"),
        ),
        migrations.AlterField(
            model_name='transfert',
            name='last_namesender',
            field=models.CharField(max_length=50, verbose_name="Nom de l' expediteur"),
        ),
    ]
