# Generated by Django 5.1.6 on 2025-04-11 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_documentprocessstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]
