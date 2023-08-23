from django.db import models

class Product(models.Model):
    products_id = models.AutoField(primary_key=True)
    products_name = models.CharField(max_length=100)
    products_price = models.DecimalField(max_digits=10, decimal_places=2)
    products_description = models.TextField()
    products_image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.products_name