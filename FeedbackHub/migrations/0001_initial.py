# Generated by Django 5.0.4 on 2024-05-06 00:26

import django.db.models.deletion
from django.db import migrations, models

def cargar_tipos_mensaje(apps, schema_editor):
    TipoMensaje = apps.get_model('FeedbackHub', 'TipoMensaje')
    TipoMensaje.objects.bulk_create([
        TipoMensaje(tipo='Queja'),
        TipoMensaje(tipo='Sugerencia'),
        TipoMensaje(tipo='Reclamo')
    ])

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoMensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=11, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('correo_electronico', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'unique_together': {('nombre', 'correo_electronico')},
            },
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asunto', models.CharField(max_length=250)),
                ('contenido', models.TextField()),
                ('fecha', models.DateField(auto_now=True)),
                ('hora', models.TimeField(auto_now=True)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FeedbackHub.tipomensaje')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FeedbackHub.usuario')),
            ],
        ),
        migrations.RunPython(cargar_tipos_mensaje),
    ]
