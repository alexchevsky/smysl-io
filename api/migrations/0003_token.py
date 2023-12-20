# Generated by Django 4.0 on 2023-11-24 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_is_available_task_is_public'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('token', models.CharField(default='10d2aae821d14d61', max_length=16, unique=True)),
                ('expires_at', models.DateTimeField()),
            ],
        ),
    ]