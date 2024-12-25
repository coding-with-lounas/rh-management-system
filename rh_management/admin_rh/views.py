from django.shortcuts import render,redirect,get_object_or_404
from .models import Employe,Service
from .forms import EmployeForm
from django.contrib import messages

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

# methode supprimer Employe 
def supprimerEmploye(request, pk):
    employe = Employe.objects.get(id=pk)
    if request.method== 'POST':
        try:
            employe.delete()
            messages.success(request, "L'employé a été supprimé avec succès.")
            return redirect('empList')
        except Employe.DoesNotExist:
            messages.error(request, "L'employé n'a pas été trouvé.")
            return redirect('empList')
    
    return render(request,'testsuppemp.html',{'emp':employe})


# def supprimerEmploye(request, pk):
#     # importe l'objet employe , ou raise a 404 error si non trouvé
#     employe = get_object_or_404(Employe, id=pk)
#     if request.method == 'POST':
#         employe.delete()
#         messages.success(request, "L'employé a été supprimé avec succès.")
#         return redirect('empList')
#     else:
#         messages.error(request, "L'employé n'est pas valide pour suppression.")
#         return redirect('empList')

#     # si le request method est GET, allez the confirmation page
#     return render(request, 'testsuppemp.html', {'emp': employe})


def modifierEmploye(request,pk):
    emp=Employe.objects.get(id=pk)
    if request.method=='POST':
        formEmp=EmployeForm(request.POST,instance=cmd)
        if formEmp.is_valid():
            formEmp.save()
            return redirect("empList")
        else:
            return render(request, 'empEdit.html', {"form": formEmp})
    else:
        formEmp=EmployeForm(instance=cmd)
        return render(request,'empEdit.html',{"form":formEmp})

    
# def afficherServices(request):
#     Services=