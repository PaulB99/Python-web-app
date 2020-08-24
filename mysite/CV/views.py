from django.shortcuts import render

# Create your views here.

# The CV page

def cv_page(request):
    return render(request, 'cv_base.html', {
        'new_ed_item_text': request.POST.get('ed_item_text', ''),
    })