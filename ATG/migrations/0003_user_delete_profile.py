# Generated by Django 5.0 on 2023-12-08 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ATG', '0002_alter_profile_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('line1', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('pincode', models.IntegerField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
