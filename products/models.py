from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    brand = models.CharField(max_length=255 ,null=True, blank=True)
    min_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    max_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    min_quantity = models.IntegerField( null=True, blank=True)
    max_quantity = models.IntegerField( null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to="products/", null=True, blank=True)
    thumbnail_image = models.ImageField(upload_to="products/", null=True, blank=True)

    def __str__(self):
        return self.name



User = get_user_model()


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through="CartItem")


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
