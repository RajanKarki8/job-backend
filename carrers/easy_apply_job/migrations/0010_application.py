# Generated by Django 5.0.1 on 2024-01-19 09:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easy_apply_job', '0009_alter_job_options_alter_job_requirements'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='easy_apply_job.job')),
            ],
        ),
    ]
