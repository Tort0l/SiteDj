# Generated by Django 4.2.16 on 2024-11-15 07:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique_for_date='posted', verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Краткое содержание')),
                ('content', models.TextField(verbose_name='Полное содержание')),
                ('posted', models.DateTimeField(db_index=True, default=datetime.datetime(2024, 11, 15, 10, 19, 28, 725674), verbose_name='Опубликовать')),
            ],
            options={
                'verbose_name': 'Статья блога',
                'verbose_name_plural': 'статьи блога',
                'db_table': 'Posts',
                'ordering': ['-posted'],
            },
        ),
    ]
