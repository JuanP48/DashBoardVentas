# Generated by Django 5.0.3 on 2024-04-01 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarroModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=120)),
                ('cantidad', models.IntegerField()),
                ('pais', models.CharField(max_length=120)),
                ('precio', models.IntegerField()),
                ('colorCarro', models.CharField(choices=[('rojo', 'Rojo'), ('negro', 'Negro'), ('blanco', 'Blanco'), ('gris', 'Gris')], default='', max_length=10)),
            ],
        ),
    ]