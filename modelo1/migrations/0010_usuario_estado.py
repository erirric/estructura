# Generated by Django 5.1.2 on 2024-10-27 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo1', '0009_alter_usuario_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='estado',
            field=models.CharField(default='Espera', max_length=10),
        ),
    ]
