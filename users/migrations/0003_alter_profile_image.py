# Generated by Django 4.2.5 on 2023-10-26 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIcAAACHCAMAAAALObo4AAAAY1BMVEX///8AAADs7OwdHR3z8/P39/fm5uZgYGAlJSX8/PzKysovLy+urq7g4OBkZGSYmJiBgYFvb2/U1NQ6OjpOTk5DQ0N1dXWkpKQRERG6urrCwsIqKipaWlp7e3tpaWk1NTWKiorw5FJVAAADHUlEQVR4nO2b63aqMBBGCQICBeTq3db3f8qatraiQGZCvnDOWtm/XbpXmGQuRM9zOBwOh8Ph+M8IA9/3g2RZiXxXrrt4derWZeYvJRHtRI84CxawCK+xeKbJrD+f9O3FQnKO7GqUgxaSzKJFMq5hVWRKQ4idLY3LpIa1FTkoNITIbWgEK6VHa2P7FkoNITZ4jZSgIWL8MdJSPESJ1qhJGkKgU41qz94BR4i/J3p02AVRnx13aqhHRfaARmrYkD06pAd1t9xYIR8MPTyEOAI9rgwP5M5dMzwKoIc61f7xBvRgaAjhPJzHQh7UbCvZAz0458cZ6LFheCDP0yPDA5lf/OEuf4gTtGSn10HI9ELsXuCP5VaQdUSNBtw4UCuhA1bD82iRGqM1iFsXGx1fUGrDK17DC89KjdbKIDVQelgaLfuvE9xHYmsT7nzqFGmsTMe+Ccb7S3Cj/8xuRMPa8PRONLRtbI/Xv0ifk2+VLmAhCbPLPVCaSxba/OngUPbWPojyOq1zvxed0WUD3rvHW5qLVcufngR4UPeTW4qpIyJ//4lZnMZvub4vxzZGVP72OBXqJOl1DduhuVO9ffzIO2bc/zLgL4/53y8l+fHl9dAHYEXCoUly3BXlJsuyTVl0Q8mvNb5tEnrH8IjpbBPSXjMMYHRFfHUNNsaHwTIg0F4NYbLB9GdYSAytSH6a6bE3MuLOOUPTEQyIMEb7E8yuTDiTlylmNnj0OYOKWY13ZExj3q7Zqr+ezFZfY+7B0Uf/hOeMKdVoV4oJdQhFo9Mti8xtlm90DxHKDQsOmqPM0LCGEHqd1lgrrY9WE65fgo3S6iyImQTXRyfv6hXG01R8jWh6CKaHxr2hDKChc8WN/qaFA/slNyJKJdxI5dxs4HDlaQSIKJXEvEYTE6USXqSaP0vvtBwNVJRKOJE6feF2HpwLXUANzv0DzrUoPuROJuFcJ+CzptapJrunIajJDrlbJNQdY7pOf4Zat/8rzyUw2z89Q59l4rKLhJFhkBt3TdfwwneYRsHrHeqqWZmnqfidg/wfmGmW+AOVw+FwOBwOxzCfqScpMSBoCf8AAAAASUVORK5CYII=', upload_to='profile_picture'),
        ),
    ]
