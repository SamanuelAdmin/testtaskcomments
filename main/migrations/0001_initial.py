# Generated by Django 4.2.1 on 2024-10-20 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('homepage', models.URLField(blank=True)),
                ('text', models.TextField()),
                ('time_create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
