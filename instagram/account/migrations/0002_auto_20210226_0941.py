# Generated by Django 2.2 on 2021-02-26 09:41

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.ImageField(upload_to=main.models.image_file_path),
        ),
    ]
