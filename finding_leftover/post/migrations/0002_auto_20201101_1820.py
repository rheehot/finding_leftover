# Generated by Django 3.1.2 on 2020-11-01 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='media/default_image.jpeg', upload_to='post'),
        ),
    ]
