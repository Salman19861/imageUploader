# Generated by Django 3.2.9 on 2022-03-01 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='imgModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='allImages')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
