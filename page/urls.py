from django.urls import path
from .views import index, product_details,dressing_cabin, \
    sub_category_details, category_details, about, contact

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('dressing-cabin/', dressing_cabin, name="dressing_cabin"),

    path('product-details/<slug:slug>', product_details, name="product_details"),

    path('sub-categories/<slug:slug>/', sub_category_details, name="sub_category_details"),
    path('categories/<slug:slug>/', category_details, name="category_details"),   
]
