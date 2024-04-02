from django.shortcuts import render, redirect
from blogs.models import Category, blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, blogPostForm, FinalManagerblogPostForm
from django.template.defaultfilters import slugify
from django.shortcuts import get_object_or_404

import random
import string

# Create your views here.


@login_required(login_url='login')
def dashboards(request):
    category_count = Category.objects.all().count()
    blog_count = blog.objects.all().count()

    context = {

        'category_count': category_count,
        'blog_count': blog_count,

    }
    return render(request, 'Dash/dashboard.html', context)


def dashcategories(request):
    return render (request, 'Dash/dashcategories.html' )


def addcategory(request):
    if request.method =='POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashcategories')
    form = CategoryForm()
    
    context = {

        'form': form,

    }
    
    return render (request, 'Dash/addcategory.html', context )


def editcategory(request, pk):
    catego = get_object_or_404(Category, pk=pk)
    if request.method=='POST':
        form = CategoryForm(request.POST, instance=catego)
        if form.is_valid():

            form.save()
            return redirect('dashcategories')

    form = CategoryForm(instance=catego)
    

    context = {

        'form': form,
        'catego': catego, 
    }
    return render(request, 'Dash/editcategory.html', context)


def deletecategory(request, pk):
    catego = get_object_or_404(Category, pk=pk)
    catego.delete()
    return redirect('dashcategories')




def post(request):
    thepost = blog.objects.all()

    data = {
        'thepost': thepost,
    }
    return render(request, 'Dash/post.html', data)



def generate_random_string(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def Addpost(request):
    if request.method == 'POST':
        form = blogPostForm(request.POST, request.FILES) #added request.files bcos we would be uploading image
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
           
            title = form.cleaned_data['title']
            random_suffix = generate_random_string()
            post.slug = slugify(title) + '-' + random_suffix #i appended + '-' + random_suffix   so that i would have a unique slug even if someone tries to add blog with same title
            post.save()
            return redirect('post')
        else:
            print('Form is not valid')
            print(form.errors)
    form = blogPostForm()
    context = {
        'form': form,
    }
     
    return render(request, 'Dash/Addpost.html', context)



def AddpostFinalManager(request):
    if request.method == 'POST':
          
          form = FinalManagerblogPostForm(request.POST)
          if form.is_valid():
            form.save()
            return redirect('post')
    form = blogPostForm()
    context = {
        'form': form,
    }


    return render(request, 'Dash/AddpostFinalManager.html')


def editPost(request, pk):
    post = get_object_or_404(blog, pk=pk) #getting the value of the post that has the pk
    if request.method == 'POST':
        form = blogPostForm(request.POST, request.FILES, instance=post)  # prepopulating the fields with the intance
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug= slugify(title) + '-'+str(post.id) #in the add post i used random string but in this i am using slugify to generate slug
            post.save()
            return redirect('post')

        
    form = blogPostForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'Dash/editPost.html', context )




#restrict editor from deleting
def deleteost(request, pk):
    theblog = get_object_or_404(blog, pk=pk)
    theblog.delete()
    return redirect('post')
