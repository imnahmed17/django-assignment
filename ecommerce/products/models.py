from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    products_id = models.AutoField(primary_key=True)
    products_name = models.CharField(max_length=100)
    products_price = models.DecimalField(max_digits=10, decimal_places=2)
    products_rating = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True)
    products_description = models.TextField()
    products_image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.products_name
    

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    review_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_user = models.CharField(max_length=50, null=True, blank=True)
    review_rating = models.DecimalField(max_digits=2, decimal_places=1)
    review_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review_product.products_name
    
    def formatted_created_at(self):
        return self.created_at.strftime('%d %b %Y')