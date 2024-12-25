from django.shortcuts import render,redirect
from .models import Employe,Service
from .forms import EmployeForm
# Create your views here.

def afficherEmploye(request):
    employe= Employe.objects.all()
    return render(request,'testdjango.html',{'Employe':employe})



def ajouterEmploye(request):
    if request.method == 'POST':
        form = EmployeForm(request.POST)
        if form.is_valid():
            form.save()
            form = EmployeForm()  # Réinitialiser le formulaire
            mssg = "Commande envoyée, vous pouvez saisir une autre."
            # return render(request, 'testaddemp.html', {'formEmp': form, 'messgEmp': mssg})
            return redirect('empList')
        else:
            mssg = "Erreur : Veuillez corriger les erreurs dans le formulaire."
            return render(request, 'testaddemp.html', {'formEmp': form, 'messgEmp': mssg})
    else:
        form = EmployeForm()
        mssg = "Veuillez remplir les champs."
        return render(request, 'testaddemp.html', {'formEmp': form, 'messgEmp': mssg})

# def supprimerEmploye(request):
#     query=



    
    
    
# def afficherServices(request):
#     Services=