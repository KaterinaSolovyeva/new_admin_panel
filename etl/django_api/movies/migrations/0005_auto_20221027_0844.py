# Generated by Django 3.2 on 2022-10-27 08:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_add_role_choises'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmwork',
            name='type',
            field=models.CharField(blank=True, choices=[('movie', 'movie'), ('tv_show', 'tv_show')], max_length=20, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='personfilmwork',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personfilmwork', to='movies.person', verbose_name='Person'),
        ),
        migrations.AlterField(
            model_name='personfilmwork',
            name='role',
            field=models.CharField(choices=[('writer', 'writer'), ('actor', 'actor'), ('director', 'director')], max_length=20, verbose_name='role'),
        ),
    ]
