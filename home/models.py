from django.db import models
from django.contrib.auth.models import User
import uuid

class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class PizzaCategory(BaseModel):
    category_name = models.CharField(max_length=30)

class Pizza(BaseModel):
    category = models.ForeignKey(PizzaCategory, on_delete=models.CASCADE, related_name="category")
    pizza_name = models.CharField(max_length=30)
    price = models.IntegerField(default=100)
    image = models.ImageField(upload_to='pizza')

class Cart(BaseModel):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='carts')
    is_paid = models.BooleanField(default=False)

class CartItems(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name='cart_items')



