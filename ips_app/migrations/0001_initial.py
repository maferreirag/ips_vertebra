# Generated by Django 4.2.1 on 2023-05-30 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('archivo', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroError',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paso', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('imagen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ips_app.imagen')),
            ],
        ),
        migrations.CreateModel(
            name='HistorialProcesamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paso', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=20)),
                ('tiempo_inicio', models.DateTimeField()),
                ('tiempo_fin', models.DateTimeField()),
                ('duracion', models.DateTimeField()),
                ('imagen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ips_app.imagen')),
            ],
        ),
    ]
