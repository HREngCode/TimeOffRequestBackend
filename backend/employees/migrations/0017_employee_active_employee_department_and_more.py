# Generated by Django 4.1.3 on 2022-12-30 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supervisors', '0006_remove_supervisor_supervisor_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employees', '0016_remove_employee_employee_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='active',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='hire_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='pto_balance',
            field=models.DecimalField(decimal_places=4, max_digits=7, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='supervisor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='supervisors.supervisor'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]