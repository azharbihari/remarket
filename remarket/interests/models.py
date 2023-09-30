from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Interest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='interests')
    is_accepted = models.BooleanField(default=False)
    message = models.TextField(
        default="I'm interested in your product. Please provide more details.")
    viewed_by_seller = models.BooleanField(default=False)
    seller_response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def accept(self):
        self.is_accepted = True
        self.save()

    def mark_viewed(self):
        self.viewed_by_seller = True
        self.save()

    def respond(self, response_text):
        self.seller_response = response_text
        self.save()

    class Meta:
        unique_together = ('user', 'product')
