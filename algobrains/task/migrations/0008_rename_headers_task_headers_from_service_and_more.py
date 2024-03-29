# Generated by Django 4.2.1 on 2024-01-17 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_task_year_in_school'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='headers',
            new_name='headers_from_service',
        ),
        migrations.RemoveField(
            model_name='task',
            name='year_in_school',
        ),
        migrations.AddField(
            model_name='task',
            name='method',
            field=models.CharField(blank=True, choices=[('GET', 'GET'), ('POST', 'POST')], max_length=8),
        ),
        migrations.AddField(
            model_name='task',
            name='url',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
