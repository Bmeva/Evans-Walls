from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import blog, Category

# Create your views here.


def post_by_category(request, category_id):
    # fetch all post  that belongs to the Category with the category_id 
    thepost = blog.objects.filter(status='Published', b_category = category_id) #b_category is calling from the blog model. we used category-id becouse category in the blog model is a foreign key 
    #categories = Category.objects.all() # i added this becouse on the base.html we have categories but i rremoved it after adding the contetex processor
    try:

        thecategory = Category.objects.get(id = category_id)
    #thecategory = get_object_or_404(Category, id=category_id ) #I can also use this then i dont need the try and except block
        #Create the 404 error page and then set debug = False and allowed host as ['*']
    except:
        
       return redirect('home')
    context = {
        'thepost': thepost,
        'thecategory': thecategory,
        #'categories': categories,
    }
    return render(request, 'blogs/post_by_category.html', context)