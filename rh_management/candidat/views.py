from django.shortcuts import render, redirect
from .forms import CandidatForm
from admin_rh.models import Recrutement


def candidat_create_view(request):
    recrutements = Recrutement.objects.all()
    if request.method == 'POST':
        form = CandidatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('candidat_success')
    else:
        form = CandidatForm()
    return render(request, 'candidat_form.html', {'form': form, 'recrutements': recrutements})


def candidat_success_view(request):
    return render(request, 'candidat_success.html')
