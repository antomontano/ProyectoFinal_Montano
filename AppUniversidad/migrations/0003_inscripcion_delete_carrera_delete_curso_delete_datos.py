# Generated by Django 4.0.4 on 2022-05-26 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUniversidad', '0002_rename_carrera_carrera_nombrecarrera'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Materia', models.CharField(max_length=1)),
                ('Mesa', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Carrera',
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Datos',
        ),
    ]
