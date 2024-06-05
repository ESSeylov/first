from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    brand = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f'ID:{self.id} {self.brand} {self.name}'