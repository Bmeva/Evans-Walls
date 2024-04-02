from django.urls import path
from .import views

urlpatterns = [

        
   path('', views.dashboards, name='dashboards'),

   path('dashcategories', views.dashcategories, name='dashcategories'),


   path('dashcategories/addcategory', views.addcategory, name='addcategory'),

 #dashcategories is the dashboard category section and on the base.html i said if url contain dashcategories
 #then it should hightlight. so i inluded dashcategories in all url that is related to categories
    
   path('dashcategories/editcategory/<int:pk>/', views.editcategory, name='editcategory'),

   path('dashcategories/deletecategory/<int:pk>/', views.deletecategory, name='deletecategory'),
  


  #Blogpost crud

   path('allpost/post', views.post, name='post'),

   path('allpost/Addpost', views.Addpost, name='Addpost'),


   path('allpost/AddpostFinalManager', views.AddpostFinalManager, name='AddpostFinalManager'),

   
   path('allpost/editPost/<int:pk>/', views.editPost, name='editPost'),


   path('allpost/deleteost/<int:pk>/', views.deleteost, name='deleteost'),
  




    
] 
