from django.db import models
import datetime 

class Blog(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    message = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=datetime.datetime.now())
