# Generated by Django 5.1.3 on 2024-12-07 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='published_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
