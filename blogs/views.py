from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import blog, Category, About
from django.db.models import Q

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



def single_blog(request, id):

    single_theblog = get_object_or_404(blog, pk=id, status = 'Published') 
    data = {
        'single_theblog': single_theblog,
    }

    return render(request, 'blogs/single_blog.html', data)




def search(request):
    
    thesearchterm = request.GET.get('keyword')

    theblog = blog.objects.filter(Q(title__icontains = thesearchterm) | 
                                  Q(short_description__icontains=thesearchterm) | 
                                  Q(blog_body__icontains=thesearchterm), status='Published')
    
    
    thecategory = Category.objects.filter(Q(category_name__icontains = thesearchterm) | 
                                  Q(category_decription__icontains=thesearchterm) ) 
                                  
    
  
    context = {
        'theblog': theblog,
        'thesearchterm': thesearchterm,
        'thecategory': thecategory,
    }
    
    return render(request, 'blogs/search.html', context)





def search23(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        # Make sure keyword is not empty
        if keyword:
            theblog = blog.objects.filter(title__icontains=keyword)
        else:
            theblog = blog.objects.none()
    else:
        theblog = blog.objects.none()

    context = {
        'theblog': theblog,
        'keyword': keyword  # Pass the keyword back to the template for display
    }

    return render(request, 'blogs/search.html', context)




def about(request):

    myabout = get_object_or_404(About) 
    
    data = {
        'myabout': myabout,
    }


    return render(request, 'blogs/about.html', data)