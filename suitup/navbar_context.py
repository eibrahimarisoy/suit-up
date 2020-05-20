from product.models import SubCategory

def nav_data(request):
    context = dict()

    categories = SubCategory.objects.filter(
        status="published",
    )
    women_categories = categories.filter(gender="women")[:5]
    men_categories = categories.filter(gender="men")[:5]
    unisex_categories = categories.filter(gender="unisex")[:5]

    context['men_categories'] = men_categories
    context['women_categories'] = women_categories
    context['unisex_categories'] = unisex_categories
    return context

