from django.db import models

# Create your models here.

class cakes(models.Model):
    
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    image = models.ImageField()
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        
        verbose_name = 'cake'
        verbose_name_plural = 'cakes'
        
    def __str__(self):
        return self.name
    
    