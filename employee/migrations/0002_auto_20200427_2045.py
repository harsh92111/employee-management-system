# Generated by Django 3.0.5 on 2020-04-27 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='position',
            old_name='titile',
            new_name='title',
        ),
    ]