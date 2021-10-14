from django.db import models
from django.urls import reverse


class Supercategory(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Supercategory'
        verbose_name_plural = 'Supercategories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('online:product_list_by_category', args=[self.slug])
class Category(models.Model):
    supercategory = models.ForeignKey(Supercategory, related_name='categories', on_delete=models.CASCADE)
    super = models.SlugField(max_length=100, db_index=True)
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('super','name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('online:product_list_by_category', args=[self.slug])


class Product(models.Model):
    supercategory = models.ForeignKey(Supercategory, related_name='categories2', on_delete=models.CASCADE)
    super=models.SlugField(max_length=100, db_index=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.FileField(upload_to='products/%Y/%m/%d', blank=True)
    discount = models.PositiveIntegerField(default=0,blank=True)
    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('online:product_detail', args=[self.id])

class LoginInfo(models.Model):
    userid=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=20)
    useremail = models.EmailField()