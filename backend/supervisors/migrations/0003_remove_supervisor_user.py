# Generated by Django 4.1.3 on 2022-11-13 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supervisors', '0002_supervisor_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supervisor',
            name='user',
        ),
    ]
