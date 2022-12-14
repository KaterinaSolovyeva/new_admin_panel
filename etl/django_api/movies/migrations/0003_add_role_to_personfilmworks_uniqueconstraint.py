# Generated by Django 3.2 on 2022-10-14 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_fixed_differences_in_databases'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='personfilmwork',
            name='film_work_person_idx',
        ),
        migrations.AddConstraint(
            model_name='personfilmwork',
            constraint=models.UniqueConstraint(fields=('film_work', 'person', 'role'), name='film_work_person_role_idx'),
        ),
    ]
