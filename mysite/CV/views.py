from django.shortcuts import redirect, render
from CV.models import Qualification

# Create your views here.

# The CV page

def cv_page(request):
    if request.method == 'POST':
        Qualification.objects.create(text=request.POST['ed_item_text'])
        return redirect('/cv')

    quals = Qualification.objects.all()
    return render(request, 'cv_base.html', {'quals' : quals})
