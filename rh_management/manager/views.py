from django.shortcuts import render, redirect
from .forms import ÉvaluationForm
from .models import Évaluation
from admin_rh.models import Employe

def evaluation_create(request):
    employes = Employe.objects.all()
    if request.method == 'POST':
        form = ÉvaluationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('evaluation_success')
    else:
        form = ÉvaluationForm()
    
    return render(request, 'evaluation_form.html', {'form': form, 'employes': employes})

def evaluation_success(request):
    return render(request, 'evaluation_success.html')








# Create your views here.
# def liste_evaluations(request):
#     evaluations = Évaluation.objects.all()
#     return render(request, 'liste.html', {'evaluations': evaluations})

# def ajouter_evaluation(request):
#     if request.method == 'POST':
#         form = ÉvaluationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('liste_evaluations')
#     else:
#         form = ÉvaluationForm()
#     return render(request, 'ajouter.html', {'form': form})

# def modifier_evaluation(request, pk):
#     evaluation = get_object_or_404(Évaluation, pk=pk)
#     if request.method == 'POST':
#         form = ÉvaluationForm(request.POST, instance=evaluation)
#         if form.is_valid():
#             form.save()
#             return redirect('liste_evaluations')
#     else:
#         form = ÉvaluationForm(instance=evaluation)
#     return render(request, 'modifier.html', {'form': form})

# def supprimer_evaluation(request, pk):
#     evaluation = get_object_or_404(Évaluation, pk=pk)
#     if request.method == 'POST':
#         evaluation.delete()
#         return redirect('liste_evaluations')
#     return render(request, 'supprimer.html', {'evaluation': evaluation})
