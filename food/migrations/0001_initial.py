# Generated by Django 4.2.5 on 2023-10-17 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.TextField(max_length=75)),
                ('item_des', models.TextField(max_length=75)),
                ('item_price', models.IntegerField()),
            ],
        ),
    ]