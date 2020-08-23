from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# The CV page
def cv_page(request):
    return HttpResponse('<html><title>My CV</title></html>')
