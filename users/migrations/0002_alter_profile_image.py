# Generated by Django 4.2.5 on 2023-10-26 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='picture/profile.png', upload_to='profile_picture'),
        ),
    ]
