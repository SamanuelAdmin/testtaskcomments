# Generated by Django 5.1.2 on 2024-10-22 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_comment_options_comment_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='image',
        ),
        migrations.AddField(
            model_name='comment',
            name='file',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
