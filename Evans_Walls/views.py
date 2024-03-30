from django.http import HttpResponse
from django.shortcuts import render, redirect
from blogs.models import Category, blog

def home(request):
    #categories = Category.objects.all() i used this to display all categories at the top of the page but after i created the context processor i removed it
    featured_post = blog.objects.filter(is_featured = True, status = 'Published').order_by('updated_at')
    post = blog.objects.filter(is_featured=False, status = 'Published')

    context = {
        #'categories': categories,
        'featured_post': featured_post,
        'post': post,

    }


    return render(request, 'home.html', context)
    
        
    #return HttpResponse('<h2>Home page</h2>')