# Generated by Django 5.0.1 on 2024-01-24 07:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobsApp', '0003_employerentity_employer_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cat', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='jobs',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='JobsApp.jobcategory'),
        ),
    ]
