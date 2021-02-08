from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=128)
    date = models.DateField()
    picture = models.FileField(upload_to='images/', blank=True)
    text = models.TextField()
