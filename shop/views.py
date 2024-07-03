from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from shop.forms import ProductModelForm, CommentModelForm, OrderModelForm
from shop.models import Category, Product, Comment


# from shop.forms import OrderModelForm


# Create your views here.


def product_list(request, category_slug=None):
    filter_type = request.GET.get('filter', '')
    search_query = request.GET.get('search', '')
    categories = Category.objects.all()

    if category_slug:
        products = Product.objects.filter(category__slug=category_slug)
        if filter_type == 'expensive':
            products = products.order_by('-price')
        elif filter_type == 'cheap':
            products = products.order_by('price')
    else:
        products = Product.objects.all()
        if filter_type == 'expensive':
            products = products.order_by('-price')
        elif filter_type == 'cheap':
            products = products.order_by('price')

    if search_query:
        products = Product.objects.filter(Q(name__icontains=search_query) | Q(category__title__icontains=search_query))
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'shop/home.html', context)


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    price_lower_bound = product.price * 0.8
    price_upper_bound = product.price * 1.2
    similar_products = Product.objects.all().filter(Q(price__lte=price_upper_bound) &
                                                    Q(price__gte=price_lower_bound)).exclude(slug=slug)

    comments = product.comments.filter(is_active=True).order_by('-created_at')

    count = product.comments.count()
    context = {
        'product': product,
        'comments': comments,
        'count': count,
        'similar_products': similar_products
    }
    return render(request, 'shop/detail.html', context)


def product_add(request):
    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')

        else:
            form = ProductModelForm()

        context = {
            'form': form
        }
        return render(request, 'shop/product.html', context)


def comment_add(request, pk):
    product = get_object_or_404(Product, id=pk)
    form = CommentModelForm()
    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            return redirect('product_detail', product.id)

    context = {
        'product': product,
        'form': form
    }
    return render(request, 'shop/detail.html', context)


def order_add(request, pk):
    # products = Product.objects.all() # [1,2,3,4,5]
    product = Product.objects.filter(id=pk).first()  # [1]
    form = OrderModelForm()
    if request.method == 'POST':
        form = OrderModelForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            return redirect('product_detail', product.id)

    context = {
        'product': product,
        'form': form
    }
    return render(request, 'shop/detail.html', context)


def delete_prt(request, pk):  # delete_prt (bu) --> delete_product (shu ma'noni bildiradi)
    product = Product.objects.filter(id=pk).first()
    if product:
        product.delete()
        return redirect('products')

    conntext = {
        'product': product
    }
    return render(request, 'shop/detail.html', conntext)


def edit_prt(request, pk):  # edit_prt (bu) --> edit_product (shu ma'noda ishlatilgan)
    product = Product.objects.get(id=pk)
    form = ProductModelForm(instance=product)
    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('detail', product.id)

    context = {
        'form': form,
        'product': product
    }
    return render(request, 'shop/update-product.html', context)
