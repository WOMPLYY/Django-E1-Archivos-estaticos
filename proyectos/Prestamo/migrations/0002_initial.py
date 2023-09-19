# Generated by Django 4.2.4 on 2023-09-19 21:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Prestamo', '0001_initial'),
        ('Inventario', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='herramienta',
            field=models.ManyToManyField(to='Prestamo.herramienta'),
        ),
        migrations.AddField(
            model_name='herramienta',
            name='Inventario_herramienta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.inventario_herramienta'),
        ),
    ]
