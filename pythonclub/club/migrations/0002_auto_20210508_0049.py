# Generated by Django 3.2.2 on 2021-05-08 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='meetingminutes',
            name='meetingid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='club.meeting'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]