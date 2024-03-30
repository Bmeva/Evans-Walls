from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length = 50, unique=True)
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now_add =True)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.category_name
    
STATUS_CHOICES = (
    ('Draft', 'Draft'),
    ('Published', 'Published')
)

class blog(models.Model):
    title = models.CharField(max_length = 48)
    slug = models.SlugField(max_length = 150, unique = True, blank = True)
    b_category = models.ForeignKey(Category, on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d', blank=True)
    short_description = models.TextField(max_length = 500)
    blog_body = models.TextField(max_length = 2500)
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default='Draft')
    is_featured = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now_add =True)

    class Meta:
        verbose_name_plural = 'Blogs'
    
    def __str__(self):
        return self.title