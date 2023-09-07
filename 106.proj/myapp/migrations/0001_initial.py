# Generated by Django 3.2.11 on 2023-08-18 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('page_name', models.CharField(max_length=70)),
                ('page_cat', models.CharField(max_length=70)),
                ('page_publish_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('newpage', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.page')),
                ('likes', models.IntegerField()),
            ],
            bases=('myapp.page',),
        ),
    ]
