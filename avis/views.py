from django.shortcuts import render

# Create your views here.

def allavis(request):
    return render(request, 'avis/allavis.html')
