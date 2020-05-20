from django.db import models

# Create your models here.

DEFAULT_STATUS = "draft"

STATUS = [
    # left side: DB
    # right side: human-readable name => DB de standart olması için soldaki bilgi DB için
    ('draft', 'Taslak'),
    ('published', 'Yayinlandi'),
    ('deleted', 'Silindi'),
]

GENDER_CHOICE = [
    ('men', 'Erkek'),
    ('women', 'Kadin'),
    ('unisex', 'Unisex'),
]

# Category
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=200, 
        default="",
    )
    cover_image = models.ImageField(
        upload_to='category',
        null=True,
        blank=True,
        help_text="800*533px"
    )
    status = models.CharField(
        default=DEFAULT_STATUS, 
        choices=STATUS,
        max_length=10,
    )

    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{1000 + self.pk} - {self.title}"

    class Meta:
        ordering = ['title']

class SubCategory(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(
        max_length=200, 
        default="",
    )
    cover_image = models.ImageField(
        upload_to='category',
        null=True,
        blank=True,
        help_text="800*533px"
    )
    status = models.CharField(
        default=DEFAULT_STATUS, 
        choices=STATUS,
        max_length=10,
    )
    gender = models.CharField(
        max_length=6,
        default="unisex",
        choices=GENDER_CHOICE,
    )
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.category} - {self.gender} - {self.title}"

    class Meta:
        ordering = ['id']


# Product
class Product(models.Model):
    sub_category = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=200, 
        default="",
    )
    content = models.TextField() 
    stock = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    price = models.FloatField(blank=True, null=True) # 199.29
    is_home = models.BooleanField(default=False, blank=True, null=True)
    status = models.CharField(
        default=DEFAULT_STATUS, 
        choices=STATUS,
        max_length=10,
    )
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CoverImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='product', verbose_name='Image')
