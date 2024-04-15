# Generated by Django 5.0.4 on 2024-04-15 14:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0002_reserva_clase_alter_reserva_seccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='clase',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to='grupos.clase'),
        ),
    ]
