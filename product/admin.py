from django.contrib import admin
from .models import Category, Product, CoverImages, SubCategory

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'pk',
        'title',
        'slug',
        'status',
        'updated_at', 
    )
    list_filter = ('status',)
    list_editable = (
        'title',
        'status',
    )


class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", "gender",)}
    list_display = (
        'pk',
        'title',
        'category',
        'slug',
        'gender',
        'status',
        'updated_at', 
    )
    list_filter = ('status', 'gender')
    list_editable = (
        'title',
        'status',
    )


class ImageInline(admin.TabularInline):
    model = CoverImages

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'pk',
        'sub_category',
        'title',
        'slug',
        'is_home',
        'price',
        'stock',
        'status',
        'updated_at', 
    )
    list_filter = ('status',)
    list_editable = (
        'title',
        'is_home',
        'status',
        
    )
    inlines = [ImageInline,]

admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)