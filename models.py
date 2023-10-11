from django.db import models

# Create your models here.

class Images(models.Model): 
    imageId = models.CharField(max_length=50) 
    img = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.imageId