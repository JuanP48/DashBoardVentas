# Generated by Django 5.0.3 on 2024-04-01 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_usersmodel_barrio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersmodel',
            name='barrio',
            field=models.CharField(choices=[], max_length=100),
        ),
    ]
