from django.db import models
from django.utils.text import slugify


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'  # 'Kategoriyalar'


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
    slug = models.SlugField(unique=True, blank=True)
    category = models.ManyToManyField(Category, default=None)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def discount_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price

    def save(self, *args, **kwargs):
        if not self.slug:
            while True:
                self.slug = slugify(self.name) + '-1'

        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    # class Meta:
    #     verbose_name_plural = 'Commodities'  # 'Mahsulotlar'


class Order(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    quantity = models.PositiveIntegerField(default=1)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='orders')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Comment(models.Model):
    full_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    body = models.TextField()
    # is_possible = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='comments')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.full_name} => by comment'

    # class Meta:
    #     verbose_name_plural = 'Commentary'  # 'Izohlar'
