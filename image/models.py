from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='media/')


class PageView(models.Model):
    hits=models.IntegerField(default=0)