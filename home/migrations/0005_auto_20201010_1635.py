# Generated by Django 3.1.2 on 2020-10-10 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_post_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
    ]
