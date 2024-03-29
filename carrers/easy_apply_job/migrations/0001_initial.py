# Generated by Django 5.0.1 on 2024-01-16 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[('internship', 'Internship'), ('junior-developer', 'Junior-developer')], max_length=255)),
            ],
        ),
    ]
