# Generated by Django 4.2.7 on 2023-11-13 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hmsapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='blood_group',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='email',
        ),
    ]
