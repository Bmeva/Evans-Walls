from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length = 50, unique=True)
    category_decription = models.CharField(max_length = 150, unique=True, null=True)
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
    blog_body = RichTextField(blank=True, null=True)
    video = models.FileField(upload_to='videos/%Y/%m/%d', blank=True, null=True)
    #blog_body = models.TextField(max_length=4000)
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default='Draft')
    is_featured = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now_add =True)

    class Meta:
        verbose_name_plural = 'Blogs'
    
    def __str__(self):
        return self.title
    

class About(models.Model):
    about_heading = models.CharField(max_length = 25)
    about_descrip = models.TextField(max_length = 4000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.about_heading
        
class SocialLink(models.Model):
    platform = models.CharField(max_length =25)
    links = models.URLField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.platform
    
    #if you want the updated_at field to automatically update whenever the object is saved, 
    #you should use auto_now=True. auto_now_add is typically used for fields that should be set 
    #to the current date and time when the object is first created and not updated thereafter



class commentModel(models.Model):
    theuser = models.ForeignKey(User, on_delete=models.CASCADE)
    theblog = models.ForeignKey(blog, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment


