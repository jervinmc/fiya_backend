# Generated by Django 4.0.1 on 2022-05-28 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_report_is_respo'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='report_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='report_id'),
        ),
    ]