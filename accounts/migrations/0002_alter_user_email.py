# Generated by Django 4.2.7 on 2024-03-08 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=55, unique=True, verbose_name='Email Address'),
        ),
    ]
