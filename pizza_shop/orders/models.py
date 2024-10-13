from django.db import models

from .validators import users_age_validator
# Create your models here.

class User(models.Model):
    SEX_PERSON = {
        "m": "male",
        "f": "female",
    }
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=50, null=True)
    age = models.PositiveIntegerField(null=True, validators=[users_age_validator])
    sex = models.CharField(max_length=1, choices=SEX_PERSON, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


    class Meta:
        indexes = [
            models.Index(fields=["first_name"], name="first_name_index"),
            models.Index(fields=["last_name"], name="last_name_index"),
            models.Index(fields=["age"], name="age_index"),
            models.Index(fields=["sex"], name="sex_index"),
        ]

    def __str__(self):
        return f" {self.first_name} {self.last_name}"


class Buyer(User):
    byer_email = models.EmailField(null=True)

class Admin(User):
    admin_rate = models.IntegerField(null=True)

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('pizza', 'Pizza'),
        ('snack', 'Snack'),
        ('drink', 'Drink'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    ingredients = models.TextField()
    nutrition = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
    ]

    customer = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} by {self.customer}"

