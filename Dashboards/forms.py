from django import forms
from blogs.models import Category, blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



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



class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        #we did not specify password here but by default the UserCreationForm form would display it

#for the edit we can also use the same AddUserForm which inherits from the (UserCreationForm) form above but if we do then it would include the password and confirm password by default.
#so instead we create another form that inherits from ModelForm
class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')