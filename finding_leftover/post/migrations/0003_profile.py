# Generated by Django 3.1.2 on 2020-10-26 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('post', '0002_auto_20201024_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('store_name', models.CharField(blank=True, max_length=500)),
                ('store_adress', models.CharField(blank=True, max_length=30)),
                ('profile_memo', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
