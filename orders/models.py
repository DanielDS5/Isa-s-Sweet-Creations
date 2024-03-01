from django.db import models
from django.contrib.auth import get_user_model
from shop.models import Product
from django.db.models import F, Sum, FloatField

# Create your models here.

User = get_user_model()

class Order(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.id
    
    @property
    def total(self):
        return self.OrderLine_set.aggregate(
            total = Sum(F("price")*F("amount"), output_field = FloatField())
        )["total"]
    
    class Meta:
        db_table = "Orders"
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ['id']
        
class OrderLine(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "OrdersLines"
        verbose_name = "Order Line"
        verbose_name_plural = "Orders Lines"
        ordering = ['id']