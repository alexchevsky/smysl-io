# Generated by Django 4.0 on 2023-11-24 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='is_available',
            new_name='is_public',
        ),
    ]