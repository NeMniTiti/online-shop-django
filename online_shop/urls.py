
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.get_list_products, name='get_list_products'),
    path('category/', views.get_list_categories, name='get_list_categories'),
    path('category/<str:slug>/', views.get_category_detail, name='get_category_detail'),
    path('product/<int:pk>/', views.get_product_detail, name='get_product_detail'),
    # path('about/', views.about, name='about'),
    # path('cats/<int:cat_id>/', views.categories, name='cats'),
    # path('cats/<slug:cat_slug>/', views.categories_slug, name='cats_slug'),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive, name='archive'),
]