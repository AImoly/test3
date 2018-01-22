# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('atitle', models.CharField(verbose_name='当前区域', max_length=20)),
                ('aParent', models.ForeignKey(to='area.AreaInfo', null=True, blank=True)),
            ],
            options={
                'db_table': 'booktest_areainfo',
            },
        ),
        migrations.CreateModel(
            name='Pictest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('up_pics', models.ImageField(upload_to='area/')),
            ],
        ),
    ]
