from django.db import models
from django.urls import reverse
from category.models import Category # type: ignore


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    description = models.TextField(max_length=500,blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='images/products/') 
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # type: ignore
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    
    
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug,self.slug])
    
    def _str_(self):
        return self.product_name