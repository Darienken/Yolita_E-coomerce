from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.CharField(max_length=200)
    quantity = models.PositiveSmallIntegerField(default=0)
    value_to_yoli = models.DecimalField(max_digits=8, decimal_places=2)
    earnings = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.BooleanField(default=True)
    show_price = models.BooleanField(default=True)

    def __str__(self):
        return self.name