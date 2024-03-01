from django.db import models

# Create your models here.

class Post(models.Model):
    
    image = models.ImageField(upload_to = "blog")
    created = models.DateTimeField(auto_now_add=True)