# Generated by Django 3.1.2 on 2020-11-02 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20201101_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='media/default_image.jpg', upload_to='post'),
        ),
        migrations.AlterField(
            model_name='store',
            name='store_image',
            field=models.ImageField(default='media/default_image.jpg', upload_to='store'),
        ),
    ]