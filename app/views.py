from django.shortcuts import render
from .models import Gallery

def index(request):
    return render(request,'index.html')


def gallery(request):
    post = Gallery.objects.all()

    return render(request, 'gallery.html',{'post':post})

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')


def blog_list(request):
    return render(request, 'blog-list.html')

def blog_sidebar(request):
    return render(request, 'blog-sidebar.html')


def blog_details(request):
    return render(request, 'blog-details.html')


def blog_team(request):
    return render(request, 'team.html')



def contact(request):
    return render(request, 'contact.html')
