# Generated by Django 5.0.1 on 2024-01-16 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easy_apply_job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='experience',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='requirements',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='type',
            field=models.CharField(choices=[('internship', 'Internship'), ('junior-developer', 'Junior-developer'), ('mid/sinior', 'Mid/Sinior')], max_length=255),
        ),
    ]
