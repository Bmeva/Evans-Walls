from django.http import HttpResponse
from django.shortcuts import render, redirect

def home(request):


    return render(request, 'home.html')
    
    
    
    #return HttpResponse('<h2>Home page</h2>')