from django.urls import path, include
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


  path('allpost/deletepost/<int:pk>/', views.deletepost, name='deletepost'),
  



  #managing users section
#for people with managers permision to add and remove users 
  path('userMgt/allusers/', views.allusers, name='allusers'),

  path('userMgt/aaddusers/', views.aaddusers, name='aaddusers'),

   path('userMgt/editusers/<int:pk>', views.editusers, name='editusers'),

   
  path('userMgt/deleteUser/<int:pk>/', views.deleteUser, name='deleteUser'),
  





    
] 
