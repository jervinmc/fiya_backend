# Generated by Django 4.0.1 on 2022-05-27 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='is_respo',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='is_respo'),
        ),
    ]
