# Generated by Django 3.2.2 on 2021-05-14 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
                ('career', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('profile_img', models.ImageField(upload_to='profile/')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('greetings_1', models.CharField(max_length=5)),
                ('greetings_2', models.CharField(max_length=5)),
                ('picture', models.ImageField(upload_to='picture/')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
