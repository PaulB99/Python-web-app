from django.shortcuts import redirect, render
from CV.models import Qualification, Experience, Skill

# Create your views here.

# The CV page

def cv_page(request):
    if request.method == 'POST':
        if(not(request.POST.get('ed_item_text') is None)):
            Qualification.objects.create(text=request.POST['ed_item_text'])
        if(not(request.POST.get('ex_item_text') is None)):
            Experience.objects.create(text=request.POST['ex_item_text'])
        if(not(request.POST.get('sk_item_text') is None)):
            Skill.objects.create(text=request.POST['sk_item_text'])
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

    # , {'exps' : exps}, {'skills' : skills} this wants to go into render once I work out how

