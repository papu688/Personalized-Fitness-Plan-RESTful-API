# Generated by Django 5.1.1 on 2024-10-02 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0004_user_is_staff_user_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=True),
        ),
    ]
