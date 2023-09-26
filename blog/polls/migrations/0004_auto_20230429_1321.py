# Generated by Django 3.2.18 on 2023-04-29 10:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_historynews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historynews',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
