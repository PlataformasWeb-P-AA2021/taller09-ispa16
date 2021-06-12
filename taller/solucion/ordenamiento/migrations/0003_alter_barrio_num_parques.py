# Generated by Django 3.2.4 on 2021-06-11 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenamiento', '0002_alter_barrio_num_parques'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barrio',
            name='num_parques',
            field=models.IntegerField(choices=[(1, 'Uno'), (2, 'Dos'), (3, 'Tres'), (4, 'Cuatro'), (5, 'Cinco'), (6, 'Seis')], verbose_name='Numero de parques'),
        ),
    ]
