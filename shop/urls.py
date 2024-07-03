from django.contrib import admin
from django.urls import path

from shop.views import product_list, product_detail, comment_add, product_add, order_add, delete_prt, edit_prt

urlpatterns = [
    path('shopping/', product_list, name='products'),
    path('category/<slug:category_slug>', product_list, name='product_of_category'),
    path('product/<slug:slug>', product_detail, name='detail'),
    path('product-add/', product_add, name='product_add'),
    path('detail/<int:product_id>/comment', comment_add, name='comment_add'),
    path('detail/<int:pk>/order', order_add, name='order_add'),

    # DELETE and EDIT

    path('detail/<int:pk>/delete-product', delete_prt, name='delete'),
    path('detail/<int:pk>/edit-product', edit_prt, name='edit')
]
