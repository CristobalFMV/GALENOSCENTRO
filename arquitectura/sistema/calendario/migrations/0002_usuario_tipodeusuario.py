# Generated by Django 4.2.7 on 2023-11-21 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='tipodeusuario',
            field=models.CharField(choices=[('Paciente', 'Paciente'), ('Medico', 'Medico'), ('Secretaria', 'Secretaria')], default=1, max_length=40, verbose_name='tipo de usuario'),
            preserve_default=False,
        ),
    ]
