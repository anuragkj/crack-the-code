# Generated by Django 4.1 on 2023-09-12 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_alter_answer_time_submitted'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together=set(),
        ),
    ]