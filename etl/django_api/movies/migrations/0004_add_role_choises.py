# Generated by Django 3.2 on 2022-10-17 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_add_role_to_personfilmworks_uniqueconstraint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personfilmwork',
            name='role',
            field=models.CharField(choices=[('WRITER', 'writer'), ('ACTOR', 'actor'), ('DIRECTOR', 'director')], max_length=20, verbose_name='role'),
        ),
    ]
