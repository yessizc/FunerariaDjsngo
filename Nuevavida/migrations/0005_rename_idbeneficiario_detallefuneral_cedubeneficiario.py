# Generated by Django 4.1.1 on 2022-12-12 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Nuevavida', '0004_rename_idbeneficiario_detallefuneral_idbeneficiario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detallefuneral',
            old_name='idbeneficiario',
            new_name='cedubeneficiario',
        ),
    ]