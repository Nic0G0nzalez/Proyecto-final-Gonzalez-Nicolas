# Generated by Django 5.0.2 on 2024-03-09 17:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('DNI', models.IntegerField(max_length=8)),
                ('direccion', models.CharField(max_length=40, validators=[django.core.validators.RegexValidator(regex='^[0-9a-zA-Z]*$')])),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Productos_pormayor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('DNI', models.IntegerField(max_length=8)),
                ('direccion', models.CharField(max_length=40, validators=[django.core.validators.RegexValidator(regex='^[0-9a-zA-Z]*$')])),
            ],
        ),
    ]
