# Generated by Django 5.0.4 on 2024-04-15 14:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='clase',
            field=models.ForeignKey(default='Roma', on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to='grupos.clase'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='seccion',
            field=models.CharField(max_length=50),
        ),
    ]
