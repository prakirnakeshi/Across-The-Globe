# Generated by Django 5.0 on 2023-12-08 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ATG', '0005_rename_line1_user_line1_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]
