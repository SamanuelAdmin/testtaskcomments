# Generated by Django 4.2.1 on 2024-10-20 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_comment_parentcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parentComment',
            field=models.ForeignKey(blank=None, default=None, on_delete=django.db.models.deletion.CASCADE, to='main.comment'),
        ),
    ]
