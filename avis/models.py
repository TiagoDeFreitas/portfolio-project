from django.db import models

# Create your models here.
class Artikel(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')
