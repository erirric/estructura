# Generated by Django 5.1.2 on 2024-10-27 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo1', '0007_alter_usuario_apellido_alter_usuario_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='ticket',
            field=models.IntegerField(default=1, editable=False),
        ),
    ]
