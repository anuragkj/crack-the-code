# Generated by Django 4.1 on 2023-09-12 19:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_task_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='time_submitted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
