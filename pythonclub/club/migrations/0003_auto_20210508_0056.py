# Generated by Django 3.2.2 on 2021-05-08 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_auto_20210508_0049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='userid',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='meetingminutes',
            old_name='meetingid',
            new_name='meeting',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='userid',
            new_name='user',
        ),
    ]
