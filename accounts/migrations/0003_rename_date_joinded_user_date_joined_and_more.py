# Generated by Django 4.2.7 on 2024-03-09 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='date_joinded',
            new_name='date_joined',
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
