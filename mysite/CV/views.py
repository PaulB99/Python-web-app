from django.shortcuts import redirect, render
from CV.models import Qualification, Experience, Skill

# Create your views here.

# The CV page

def cv_page(request):
    if request.method == 'POST':
        Qualification.objects.create(text=request.POST['ed_item_text'])
        return redirect('/cv')

    if request.method == 'POSTex':
        Experience.objects.create(text=request.POSTex['ex_item_text'])
        return redirect('/cv')

    if request.method == 'POSTsk':
        Skill.objects.create(text=request.POSTsk['sk_item_text'])
        return redirect('/cv')

    exps = Experience.objects.all()

    quals = Qualification.objects.all()
    return render(request, 'cv_base.html', {'quals' : quals}, {'exps' : exps}, {'skills' : skills})

