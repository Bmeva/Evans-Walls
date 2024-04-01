from .models import Category
from .models import SocialLink
from .models import About



def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)


def get_social_links(request):
    social_links = SocialLink.objects.all()
    return dict(social_links=social_links)


def get_about(request):
    theabout = About.objects.all()
    return dict(theabout=theabout)