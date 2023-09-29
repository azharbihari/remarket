from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category_images/', blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')
    is_active = models.BooleanField(default=True)
    condition = models.CharField(max_length=100, choices=[(
        'new', 'New'), ('used', 'Used')], default='used')
    location = models.CharField(max_length=100)
    availability = models.CharField(max_length=100, choices=[(
        'in_stock', 'In Stock'), ('out_of_stock', 'Out of Stock')], default='in_stock')
    delivery_option = models.CharField(max_length=100, choices=[(
        'pickup', 'Pickup'), ('shipping', 'Shipping')], default='pickup')
    featured_image = models.ImageField(
        upload_to='product_images/', default='product_images/default_product_image.png')
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images/')
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, related_name='images')
