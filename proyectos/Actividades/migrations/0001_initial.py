# Generated by Django 4.2.4 on 2023-09-19 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wiki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('referencias_web', models.TextField(verbose_name='Referencias web')),
            ],
            options={
                'verbose_name': 'Wiki',
                'verbose_name_plural': 'Wikis',
                'db_table': 'wiki',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descripcion', models.TextField(verbose_name='Descripcion de la zona')),
            ],
            options={
                'verbose_name': 'Zona',
                'verbose_name_plural': 'Zonas',
                'db_table': 'zona',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Labor_social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('Wiki', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Actividades.wiki')),
            ],
            options={
                'verbose_name': 'Labor social',
                'verbose_name_plural': 'Labores sociales',
                'db_table': 'labor_social',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Cronograma_actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField(verbose_name='Fecha_inicio')),
                ('fecha_fin', models.DateField(verbose_name='Fecha_fin')),
                ('Labor_social', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Actividades.labor_social')),
                ('Zona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Actividades.zona')),
            ],
            options={
                'verbose_name': 'Cronograma actividad',
                'verbose_name_plural': 'Cronograma actividades',
                'db_table': 'cronograma_actividad',
                'ordering': ['id'],
            },
        ),
    ]
