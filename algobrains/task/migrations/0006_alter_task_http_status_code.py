# Generated by Django 4.2.1 on 2024-01-17 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_alter_task_http_status_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='http_status_code',
            field=models.IntegerField(),
        ),
    ]
