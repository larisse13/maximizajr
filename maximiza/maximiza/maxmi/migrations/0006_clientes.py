# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-09 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maxmi', '0005_auto_20190509_1943'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('image', models.ImageField(upload_to='midia/clientes', verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['title'],
            },
        ),
    ]
