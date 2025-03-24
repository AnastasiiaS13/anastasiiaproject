from django.db import models
from django.contrib.auth.models import User
from main.models import Product, Client


class Cart(models.Model):
    client = models.ForeignKey(Client, null=True, blank=True, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Client's cart {self.client}" if self.client else f"Session cart {self.session_key}"

    def save(self, *args, **kwargs):
        # Ensure that either client or session_key is filled, but not both
        if not self.client and not self.session_key:
            raise ValueError("Either 'client' or 'session_key' must be provided.")
        if self.client and self.session_key:
            raise ValueError("You can't have both 'client' and 'session_key' at the same time.")
        super().save(*args, **kwargs)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def total_price(self):
        return self.product.price * self.quantity
