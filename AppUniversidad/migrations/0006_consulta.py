# Generated by Django 4.0.4 on 2022-06-06 23:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppUniversidad', '0005_mensaje'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('titulo', models.CharField(max_length=255)),
                ('cuerpo', models.CharField(max_length=3000)),
                ('ejercicio', models.ImageField(blank=True, upload_to='ejercicio')),
            ],
        ),
    ]
