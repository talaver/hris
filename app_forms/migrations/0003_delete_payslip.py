# Generated by Django 2.2.1 on 2019-05-09 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_forms', '0002_broadcast_leaves_overtime_payslip_productivitytool_undertime_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payslip',
        ),
    ]