from django.contrib import admin
from .models import Carousel
# Register your models here.


class CarouselAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'title',
        'cover_image',
        'status',
    ]
    list_filter = ['status', ]
    list_editable = list_filter


admin.site.register(Carousel, CarouselAdmin)
