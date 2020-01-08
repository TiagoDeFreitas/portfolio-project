from django.shortcuts import render, get_object_or_404

from .models import Artikel
# Create your views here.

def allavis(request):
    posts = Artikel.objects
    return render(request, 'avis/allavis.html', {'posts':posts})

def detail(request, blog_id):
    detailblog = get_object_or_404(Artikel, pk=blog_id)
    return render(request, 'avis/detail.html', {'blog':detailblog})
