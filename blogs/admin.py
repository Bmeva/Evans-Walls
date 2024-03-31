from django.contrib import admin
from django.http.request import HttpRequest
from .models import Category, blog, About, SocialLink


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)} #this would auto generate slug as the title is typed
    list_display = ('id', 'title', 'b_category', 'status', 'author', 'is_featured')
    list_display_links = ('id', 'title', 'b_category')
    search_fields = ('id', 'title', 'author', 'b_category__category_name', 'status') #b_category__category_name is a foreign key that is why we used __ to point to the particular field
    list_editable = ('is_featured','status')
    ordering = ['id']
    

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        
        count = About.objects.all().count()
        if count == 0:
            return True
        return False
    

    
admin.site.register(Category)

admin.site.register(blog, BlogAdmin)

admin.site.register(About, AboutAdmin)

admin.site.register(SocialLink)
