# Generated by Django 3.2.11 on 2023-07-03 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('stuid', models.IntegerField(primary_key=True, serialize=False)),
                ('stuname', models.CharField(max_length=70)),
                ('stuemail', models.EmailField(max_length=70)),
                ('stupass', models.CharField(max_length=70)),
            ],
        ),
    ]
