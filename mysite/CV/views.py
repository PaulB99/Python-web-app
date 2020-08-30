from django.shortcuts import redirect, render
from CV.models import Qualification, Experience, Skill

# Create your views here.

# The CV page

def cv_page(request):
    if request.method == 'POST':
        if(not(request.POST.get('ed_item_text') is None)):
            x=request.POST['ed_item_text']
            xlist = x.split('*', 1)
            Qualification.objects.create(text=xlist[0], date=xlist[1])
        if(not(request.POST.get('ex_item_text') is None)):
            x=request.POST['ex_item_text']
            xlist = x.split('*', 1)
            Experience.objects.create(text=xlist[0], date=xlist[1])
        if(not(request.POST.get('sk_item_text') is None)):
            x=request.POST['sk_item_text']
            xlist = x.split('*', 1)
            Skill.objects.create(text=xlist[0], date=xlist[1])
        return redirect('/cv')

    exps = Experience.objects.all()

    quals = Qualification.objects.all()

    skills = Skill.objects.all()

    context = {
        'quals' : quals,
        'exps' : exps,
        'skills' : skills,

    }
    return render(request, 'cv_base.html', context)


