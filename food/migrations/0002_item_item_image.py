# Generated by Django 4.2.5 on 2023-10-19 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='data:image/png;base64,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', max_length=500),
        ),
    ]
