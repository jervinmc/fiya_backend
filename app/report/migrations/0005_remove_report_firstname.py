# Generated by Django 4.0.1 on 2022-05-28 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_report_firstname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='firstname',
        ),
    ]
