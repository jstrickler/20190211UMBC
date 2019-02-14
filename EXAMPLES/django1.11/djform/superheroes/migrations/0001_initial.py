# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-01 15:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Enemy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Power',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Superhero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('real_name', models.CharField(max_length=32)),
                ('secret_identity', models.CharField(max_length=32)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superheroes.City')),
                ('enemies', models.ManyToManyField(to='superheroes.Enemy')),
                ('powers', models.ManyToManyField(to='superheroes.Power')),
            ],
        ),
        migrations.AddField(
            model_name='enemy',
            name='powers',
            field=models.ManyToManyField(to='superheroes.Power'),
        ),
    ]
