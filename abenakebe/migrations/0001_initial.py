# Generated by Django 2.2.1 on 2019-10-28 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageJoke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=150)),
                ('image', models.FileField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='MemeJoke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=150)),
                ('image', models.FileField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='TextJoke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
    ]