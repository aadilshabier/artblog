# Generated by Django 3.1.2 on 2020-10-10 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20201009_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.FileField(blank=True, upload_to='media/'),
        ),
    ]
