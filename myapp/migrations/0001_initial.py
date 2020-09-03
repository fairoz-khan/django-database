# Generated by Django 3.1.1 on 2020-09-03 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('url', models.URLField(max_length=100, unique=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.topic')),
            ],
        ),
        migrations.CreateModel(
            name='AccessDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('webpage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.webpage')),
            ],
        ),
    ]