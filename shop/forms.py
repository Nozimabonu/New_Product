from django import forms
from django.forms import EmailField

from shop.models import Product, Comment, Order


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.FloatField()
    discount = forms.IntegerField()
    rating = forms.ChoiceField(choices=Product.RatingChoices.choices)
    quantity = forms.IntegerField()
    slug = forms.SlugField()
    image = forms.ImageField()


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = ['name', 'description', 'price', 'image', 'rating', 'discount']
        exclude = ()


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['full_name', 'email', 'body']


class OrderModelForm(forms.ModelForm):
    email = EmailField()

    class Meta:
        model = Order
        fields = ['name', 'email']
