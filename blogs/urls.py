from django.urls import path
from .import views

urlpatterns = [

    path('<int:category_id>/', views.post_by_category, name = 'post_by_category'),

    path('<int:id>', views.single_blog, name = 'single_blog'),

    path('search/', views.search, name='search'),

    path('about/', views.about, name='about'),






  
    

   

    
] 
