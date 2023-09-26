# Generated by Django 3.2.18 on 2023-03-23 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DonationPeople',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickmame', models.CharField(max_length=30)),
                ('cash', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50)),
                ('text', models.TextField()),
                ('theme', models.CharField(default='Раздумья', max_length=30)),
                ('post_date', models.DateField()),
                ('hash_tags', models.CharField(default='#default', max_length=15)),
            ],
        ),
    ]
