# Generated by Django 3.2.9 on 2022-05-26 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0008_alter_task_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]