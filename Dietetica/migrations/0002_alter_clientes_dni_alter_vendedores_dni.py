# Generated by Django 5.0.2 on 2024-03-09 17:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dietetica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='DNI',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(7), django.core.validators.MaxValueValidator(8)]),
        ),
        migrations.AlterField(
            model_name='vendedores',
            name='DNI',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(7), django.core.validators.MaxValueValidator(8)]),
        ),
    ]
