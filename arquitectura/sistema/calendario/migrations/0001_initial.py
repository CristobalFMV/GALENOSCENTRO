# Generated by Django 4.2.7 on 2023-11-21 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('rut', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
            ],
        ),
    ]
