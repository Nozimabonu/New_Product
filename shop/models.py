from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    class RatingChoices(models.IntegerChoices):
        zero = 0
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    discount = models.IntegerField(null=True, blank=True)
    rating = models.IntegerField(choices=RatingChoices.choices, default=RatingChoices.zero)
    quantity = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    category = models.ManyToManyField(Category, default=None)

    @property
    def discount_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    quantity = models.PositiveIntegerField(default=1)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='orders')
    create_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    body = models.TextField()
    is_possible = models.BooleanField(default=False)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='comments')
    create_at = models.DateTimeField(auto_now_add=True)
