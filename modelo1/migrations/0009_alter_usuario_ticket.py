# Generated by Django 5.1.2 on 2024-10-27 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo1', '0008_usuario_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='ticket',
            field=models.IntegerField(default=1),
        ),
    ]