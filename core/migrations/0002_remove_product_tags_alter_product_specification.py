# Generated by Django 5.1.6 on 2025-02-24 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.AlterField(
            model_name='product',
            name='specification',
            field=models.TextField(blank=True, null=True),
        ),
    ]
