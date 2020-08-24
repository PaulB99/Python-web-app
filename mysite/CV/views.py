from django.shortcuts import render

# Create your views here.

# The CV page

'''
def cv_page(request):

    qual = Qualification()
    qual.text = request.POST.get('ed_item_text', '')
    qual.save()

    return render(request, 'cv_base.html', {
        'new_ed_item_text': qual.text
    })
'''
def cv_page(request):
    if request.method == 'POST':
        new_ed_item_text = request.POST['ed_item_text']  
        Qualification.objects.create(text=new_ed_item_text)  
    else:
        new_ed_item_text = ''  

    return render(request, 'cv_base.html', {
        'new_ed_item_text': new_ed_item_text,  
    })