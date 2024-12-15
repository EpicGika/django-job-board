# Generated by Django 5.1.3 on 2024-12-15 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_job_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='sluug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Full Time', 'Full-Time'), ('Part Time', 'Part-Time')], max_length=50),
        ),
    ]