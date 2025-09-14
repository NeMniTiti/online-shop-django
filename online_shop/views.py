from idlelib.rpc import request_queue
from wsgiref.util import request_uri

# from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
# from django.template.loader import render_to_string

from online_shop.models import Product, Category


# function for get all products
def get_list_products(request):
    products = Product.objects.all().select_related()
    return render(request, "online_shop/get_all_products.html", {"products": products})


# function for get all categories
def get_list_categories(request):
    categories = Category.objects.all()
    return render(request, "online_shop/get_all_categories.html", {"categories": categories})


# function for get one category
def get_category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'online_shop/get_category_detail.html',{"category": category})


# function for get one product
def get_product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "online_shop/get_product_detail.html", {"product": product})


#function for create new category in DB
def create_category(request):
    pass


#function for create new product in DB
def create_product(request):
    pass



# def index(request):
#     # print(product, category)
#     # print(request.POST)
#     if request.method == 'POST':
#         title = request.POST['title']
#         price = request.POST['price']
#         description = request.POST['descrip']
#         cat_id = request.POST['cat']
#         category = Category.objects.get(id=cat_id)
#         if title and price and description and category:
#             product = Product.objects.create(
#                 title=title,
#                 price=price,
#                 description=description,
#                 cat_id=cat_id
#             )
#
#     products = Product.objects.all()
#     print(products.query, 'тут'*10)
#     for prod in products:
#         cat = prod.cat
#         print(cat.title)
#
#
#     categories = Category.objects.all()
#     context = {
#         'products': products,
#         'categories': categories,
#     }
#     # t = render_to_string('online_shop/index.html')
#     # return HttpResponse(t)
#     # print(request.GET)
#     return render(request, 'online_shop/index.html', context)



# def categories(request, cat_id):
#     return HttpResponse(f"<h1>Категории товаров</h1><p>id: {cat_id}</p>")
#
#
# def categories_slug(request, cat_slug):
#     print(request.GET)
#     return HttpResponse(f"<h1>Категории товаров</h1><p>id: {cat_slug}</p>")

#
# def archive(request, year):
#     if year > '2025':
#         raise Http404()
#     return HttpResponse(f"<h1>Архив по годам</h1><p>id: {year}</p>")
#
#
# def page_not_found(request, exception):
#     return HttpResponseNotFound('<p>Страница не найдена</p>')