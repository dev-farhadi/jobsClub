# Generated by Django 5.0.1 on 2024-01-24 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JobsApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobs',
            old_name='employer_mamad',
            new_name='employer',
        ),
    ]