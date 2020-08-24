from django.shortcuts import render

# Create your views here.

# The CV page

def cv_page(request):
    return render(request, 'cv_base.html')