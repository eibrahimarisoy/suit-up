from django.shortcuts import get_object_or_404, render
from page.models import Carousel
from product.models import Category, Product, SubCategory
# Create your views here.

STATUS = "published"

def index(request):
    context = dict()
    carousel = Carousel.objects.filter(
        status=STATUS
    ).first()
    categories = Category.objects.filter(
        status=STATUS
    )
    products = Product.objects.filter(
        status=STATUS
    )

    context['carousel'] = carousel
    context['categories'] = categories
    context['products'] = products
    return render(request, 'page/index.html', context)


def about(request):
    context = dict()

    context['banner_tag'] = "Hakkımızda"
    return render(request, 'page/about.html', context)


def contact(request):
    context = dict()

    context['banner_tag'] = "İletişim"
    return render(request, 'page/contact.html', context)


def product_details(request, slug):
    context = dict()
    product = get_object_or_404(Product, slug=slug)
    
    context['product'] = product
    return render(request, 'product/product_details.html', context)


def dressing_cabin(request):
    context = dict()
    context['banner_tag'] = "Giyinme Kabini"
    return render(request, 'page/dressing_cabin.html', context)


def sub_category_details(request, slug):
    context = dict()
    products = Product.objects.filter(
        status=STATUS,
        sub_category__slug=slug
    )

    context['sub_category'] = get_object_or_404(SubCategory, slug=slug)
    context['products'] = products
    return render(request, 'product/sub_category_details.html', context)


def category_details(request, slug):
    context = dict()
    products = Product.objects.filter(
        status=STATUS,
        sub_category__category__slug=slug,
    )

    context['category'] = get_object_or_404(Category, slug=slug)
    context['products'] = products
    return render(request, 'product/sub_category_details.html', context)


def error_404_view(request, exception):
    return render(request, 'page/page-404.html')