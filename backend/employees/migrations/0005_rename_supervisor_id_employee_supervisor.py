# Generated by Django 4.1.3 on 2022-11-11 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_rename_employee_nubmer_employee_employee_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='supervisor_id',
            new_name='supervisor',
        ),
    ]