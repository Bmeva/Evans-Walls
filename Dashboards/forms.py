from django import forms
from blogs.models import Category, blog



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'





class blogPostForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = ('title', 'b_category', 'featured_image', 'short_description',
                   'blog_body', 'status', 'is_featured', ) #limiting the fields that the editor can add




#this form renders everything in the blog model
class FinalManagerblogPostForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = '__all__'