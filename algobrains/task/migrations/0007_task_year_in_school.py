# Generated by Django 4.2.1 on 2024-01-17 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_alter_task_http_status_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='year_in_school',
            field=models.CharField(blank=True, choices=[('Audio', (('vinyl', 'Vinyl'), ('cd', 'CD'))), ('Video', (('vhs', 'VHS Tape'), ('dvd', 'DVD'))), ('unknown', 'Unknown')], max_length=100),
        ),
    ]
