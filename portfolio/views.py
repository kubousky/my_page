from django.shortcuts import render, get_object_or_404
from .models import Category, Project
from django.views.decorators.cache import never_cache


@never_cache
def home(request):
    return render(request, "home.html", {})

def about(request):
    return render(request, "about.html", {})

def contact(request):
    return render(request, "contact.html", {})


def categories(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    projects = Project.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        projects = projects.filter(category=category)
    return render(request, "portfolio/categories.html", 
                            {'category': category,
                            'categories': categories,
                            'projects': projects})


def project_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    projects = Project.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        projects = projects.filter(category=category)
    return render(request, 
                    'portfolio/projects/list.html',
                    {'category': category,
                    'categories': categories,
                    'projects': projects})

def project_detail(request, id, slug):
    project = get_object_or_404(Project,
                                id=id,
                                slug=slug)
    return render(request,
                    'portfolio/projects/detail.html',
                    {'project': project})

    

