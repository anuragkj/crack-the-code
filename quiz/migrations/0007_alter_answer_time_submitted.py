# Generated by Django 4.1 on 2023-09-12 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_answer_time_submitted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='time_submitted',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
