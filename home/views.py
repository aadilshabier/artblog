from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import generic
from .models import Post


posts_per_page = 4


def index(request, page_number=None):
    """
    Each page should contain items 4(n-1) to 4n, 
    where n is the page number
    """

    if page_number == None:
        return redirect('1/')

    posts = Post.objects.order_by('pk')[posts_per_page *
                                        (page_number-1):posts_per_page*page_number]
    if (Post.objects.count() % posts_per_page) == 0:
        pages = Post.objects.count() // posts_per_page
    else:
        pages = (Post.objects.count() // posts_per_page) + 1

    context = {"page_number": page_number, "previous": page_number-1, "next": page_number+1,
               "posts": posts, "pages": pages}
    return render(request, "home/index.html", context)
