from django.core.cache import cache
from django.shortcuts import render, get_object_or_404, redirect
from online_shop.forms import AddCategoryForm, AddProductForm
from online_shop.models import Product, Category


# function for get all products
def get_list_products(request):
    products = cache.get('list_products')

    if not products:
        products = list(Product.objects.all().select_related('category'))
        cache.set('list_products', products, timeout=300)
    return render(request, "online_shop/get_all_products.html", {"products": products})


# function for get one product
def get_product_detail(request, pk):
    product = cache.get(f'product_{pk}')

    if not product:
        product = get_object_or_404(Product, pk=pk)
        print(product)
        if product:
            cache.set(f'product_{pk}', product, timeout=300)
    return render(request, "online_shop/get_product_detail.html", {"product": product})


# function for get all categories
def get_list_categories(request):
    categories = cache.get('list_categories')

    if not categories:
        categories = Category.objects.all()
        cache.set('list_categories', categories, timeout=300)
    return render(request, "online_shop/get_all_categories.html", {"categories": categories})


# function for get one category
def get_category_detail(request, slug):
    category = cache.get(f'category_{slug}')

    if not category:
        category = get_object_or_404(Category, slug=slug)

        if category:
            cache.set(f'category_{slug}', category, timeout=300)
    return render(request, 'online_shop/get_category_detail.html', {"category": category})


# function for create new category in DB
def add_category(request):
    if request.method == "POST":
        form = AddCategoryForm(request.POST)

        if form.is_valid():
            category = Category.objects.get_or_create(title=form.cleaned_data["title"])

            return redirect('get_list_products')
        return render(request, 'online_shop/add_category.html', {'form': form})

    form = AddCategoryForm()
    return render(request, 'online_shop/add_category.html', {'form': form})


# function for create new product in DB
def add_product(request):
    if request.method == "POST":
        form = AddProductForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            price = form.cleaned_data["price"]
            description = form.cleaned_data["description"]
            category = form.cleaned_data["category"]

            Product.objects.create(
                title=title,
                price=price,
                description=description,
                category=category
            )

            return redirect('get_list_products')
    form = AddProductForm()

    return render(request, 'online_shop/add_product.html', {"form": form})
