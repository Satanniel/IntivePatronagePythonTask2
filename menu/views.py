from django.shortcuts import render
from django.template import loader
from django.urls import reverse


# View function for home page of site.
def index(request):
    # Render the HTML template index.html
    return render(request, 'index.html')
