# Generated by Django 5.1.1 on 2024-10-02 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='updated_at',
        ),
    ]
