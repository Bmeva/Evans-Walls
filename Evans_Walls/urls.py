"""
URL configuration for Evans_Walls project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name = 'home'),

     path('', views.home, name = 'home'),

  
    path('category/',include('blogs.urls')),

    path('auth/', include('authentication.urls')), # with this would be auth/ the name of the url inside authentication.urls

    #path('', include('authentication.urls')), if i leave this path empty then it would go to authentication.urls and find the urls

     path('CMS/dashboard/', include('Dashboards.urls')),

    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
