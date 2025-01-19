from django.shortcuts import render,redirect,get_object_or_404
from .models import Employe,Service,Absence,Massrouf,Contrat,Salaire
from .forms import EmployeForm,ServiceForm,AbsenceForm ,MassroufForm
from django.contrib import messages
from django.db.models import Q,Count,Sum
from datetime import datetime,timedelta, date
from django.db.models.signals import post_save
from django.dispatch import receiver
from dateutil.relativedelta import relativedelta 


# Create your views here.
# Vue pour afficher un employe

def afficherEmploye(request):
    employe= Employe.objects.all()
    return render(request,'testdjango.html',{'Employes':employe})


# Vue pour ajouter un employe
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

# vue pour supprimer Employe 
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

def rechercherEmploye(request):
    if request.method == 'GET':
        # Si 'search' n'est pas présent dans l'URL, la méthode get() retourne maintenant une chaîne vide '' au lieu de None
        query = request.GET.get('search','').strip()
        # eliminer les espaces de debut et la fin de text avec strip
        if query:
           
            employes = Employe.objects.filter(
                Q(nom__icontains=query) |
                Q(prenom__icontains=query) |
                Q(id__icontains=query) |
                Q(adresse__icontains=query) |
                Q(date_naissance__icontains=query) |
                Q(date_embauche__icontains=query)
            )

            if not employes.exists():
                message = "Aucun employe ne correspond à votre recherche." 
                return render(request, 'testdjango.html', {'Employes': Employe.objects.all(),'message':message,'search_mode': True})

            return render(request, 'testdjango.html', {'Employes':employes,'search_mode': True})
        
        return render(request, 'testdjango.html', {'Employes': Employe.objects.all(),'message': 'Veuillez entrer un terme de recherche.','search_mode': False})
    
    return render(request, 'testdjango.html', {'Employes': Employe.objects.all(),'message': 'Utilisez la méthode GET pour effectuer une recherche.','search_mode': False})





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
    emp=get_object_or_404(Employe, id=pk)
    if request.method == 'POST':
        formEmp = EmployeForm(request.POST, instance=emp)
        if formEmp.is_valid():
            formEmp.save()
            return redirect("empList")  # Rediriger après la sauvegard
        else:
            return render(request, 'testEdit.html', {"form": formEmp})
    else:
        formEmp=EmployeForm(instance=emp)
        return render(request,'testEdit.html',{"form":formEmp})



 # Vue pour afficherun service   
def afficherService(request):
    services= Service.objects.all()
    return render(request,'testservice.html',{'services':services})

 # Vue pour afficher un service avec le nombre d'employe 
def nbr_emp_par_service(request):
    emp=Service.objects.annotate(nbr_employe=Count('rel_emp'))
    
    return render(request,'testservice.html',{'services':emp})


# Vue pour ajouter un service
def ajouterService(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('serviceList')  
        else:
            return render(request, 'testaddservice.html', {'form': form})
    else:
        form = ServiceForm()
        return render(request, 'testaddservice.html', {'form': form})

# Vue pour modifier un service
def modifierService(request, pk):
    service = get_object_or_404(Service, id=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('serviceList')  # Redirection vers la liste des services
        else:
            return render(request, 'testEditservice.html', {'form': form})
    else:
        form = ServiceForm(instance=service)
        return render(request, 'testEditservice.html', {'form': form})

# Vue pour mupprimer un service
def supprimerService(request, pk):
    service = get_object_or_404(Service, id=pk)
    if request.method == 'POST':
        try:
            service.delete()
            messages.success(request, "Le service a été supprimé avec succès.")
            return redirect('serviceList')  # Redirection vers la liste des services
        except Service.DoesNotExist:
            messages.error(request, "Le service n'a pas été trouvé.")
            return redirect('serviceList')
    
    return render(request, 'testsuppservice.html', {'service': service})



def rechercherService(request):
    if request.method == 'GET':
        query = request.GET.get('search', '').strip() 

        if query:
           
            services = Service.objects.filter(
                Q(nom_service__icontains=query) | Q(description__icontains=query)
            )

            if services.exists():
                return render(request, 'testservice.html', {'services': services})
            else:
                return render(request, 'testservice.html', {'message': 'Aucun service trouvé.'})

        else:
            return render(request, 'testservice.html', {'message': 'Veuillez entrer un terme de recherche.'})
    
    return render(request, 'testservice.html', {'message': 'Utilisez la méthode GET pour effectuer une recherche.'})



# Absence

def afficherAbsences(request):
    absences = Absence.objects.all()
    return render(request, 'liste_absences.html', {'absences': absences, 'search_mode': False})


def ajouterAbsence(request):
    if request.method == 'POST':
        form = AbsenceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "L'absence a été ajoutée avec succès.")
            return redirect('listeAbsences')  # Redirige vers la liste des absences
        else:
            messages.error(request, "Erreur : Veuillez corriger les erreurs dans le formulaire.")
    else:
        form = AbsenceForm()
    return render(request, 'ajouter_absence.html', {'form': form})


def editerAbsence(request, pk):
    absence = get_object_or_404(Absence, pk=pk)
    if request.method == 'POST':
        form = AbsenceForm(request.POST, instance=absence)
        if form.is_valid():
            form.save()
            messages.success(request, "L'absence a été modifiée avec succès.")
            return redirect('listeAbsences')  # Redirige vers la liste des absences
        else:
            messages.error(request, "Erreur : Veuillez corriger les erreurs dans le formulaire.")
    else:
        form = AbsenceForm(instance=absence)
    return render(request, 'editer_absence.html', {'form': form, 'absence': absence})


def supprimerAbsence(request, pk):
    absence = get_object_or_404(Absence, pk=pk)
    if request.method == 'POST':
        try:
            absence.delete()
            messages.success(request, "L'absence a été supprimée avec succès.")
        except Exception as e:
            messages.error(request, f"Erreur lors de la suppression : {str(e)}")
        return redirect('listeAbsences')  # Redirige vers la liste des absences
    return render(request, 'supprimer_absence.html', {'absence': absence})



def rechercherAbsences(request):
    query = request.GET.get('search', '')  # Récupère le terme de recherche
    absences = Absence.objects.all()  # Récupère toutes les absences par défaut

    if query:  # Si un terme de recherche est présent
        absences = absences.filter(
            employe__nom__icontains=query
        ) | absences.filter(
            employe__prenom__icontains=query
        ) | absences.filter(
            date_Absence__icontains=query
        ) | absences.filter(
            justification__icontains=query
        )
        if not absences.exists():  # Si aucun résultat trouvé
            message = "Aucune absence ne correspond à votre recherche."
            return render(request, 'liste_absences.html', {'absences': Absence.objects.all(), 'message': message, 'search_mode': True})
    return render(request, 'liste_absences.html', {'absences': absences, 'search_mode': True})





def demande_massrouf(request, employe_id):
    employe = get_object_or_404(Employe, pk=employe_id) 
    current_year = datetime.now().year
    demandes_massrouf = Massrouf.objects.filter(employe=employe, date_demande__year=current_year)
    
    if len(demandes_massrouf) >= 2:
        # Si l'employé a déjà fait 2 demandes cette année, afficher un message d'erreur
        messages.error(request, "Vous avez déjà demandé une avance deux fois cette année.")
        return redirect('empList')  

    if request.method == 'POST':
        form = MassroufForm(request.POST)
        if form.is_valid():
            avance = form.save(commit=False)
            avance.employe = employe  # Associe l'employé automatiquement dans la vue
            avance.save()

            # Message de succès
            messages.success(request, "Votre demande d'avance a été soumise avec succès.")
            return redirect('empList')  
    else:
      
        form = MassroufForm(initial={'employe': employe})

    return render(request, 'demande_massrouf.html', {'form': form, 'employe': employe})

def calcul_salaire_mensuel():
   
    current_date = date.today()

    # Parcourir tous les contrats actifs
    contrats = Contrat.objects.filter(date_début__lte=current_date, date_fin__gte=current_date)

    for contrat in contrats:
        employe = contrat.employe
        salaire_jour = contrat.salaireJrs

        # Calculer le nombre total de jours dans le mois
        first_day_of_month = date(current_date.year, current_date.month, 1)
        last_day_of_month = (first_day_of_month + timedelta(days=31)).replace(day=1) - timedelta(days=1)
        total_days = (last_day_of_month - first_day_of_month).days + 1

        # Obtenir les jours d'absence dans le mois
        absences = Absence.objects.filter(
            employe=employe,
            date_Absence__gte=first_day_of_month,
            date_Absence__lte=last_day_of_month
        ).count()

        # Calculer le salaire brut pour le mois
        jours_travailles = total_days - absences
        salaire_mensuel = jours_travailles * salaire_jour

        # Récupérer les montants d'avance (Massrouf) pour le mois en cours
        massroufs = Massrouf.objects.filter(
            employe=employe,
            date_demande__year=current_date.year,
            date_demande__month=current_date.month
        ).aggregate(total_massrouf=Sum('montant'))['total_massrouf'] or 0

        # Calculer le salaire final
        salaire_final = salaire_mensuel - massroufs

        # Enregistrer ou mettre à jour le salaire dans la classe Salaire
        salaire, created = Salaire.objects.update_or_create(
            employe=employe,
            mois=current_date.strftime("%B"),
            annee=current_date.year,
            defaults={
                'salaireMois': salaire_final,
                'moisdetravail': current_date.month,
                'Salaire_jr': contrat
            }
        )

        print(f"Salaire calculé pour {employe.nom}: {salaire.salaireMois} DA (Absences: {absences}, Massrouf: {massroufs} DA)")


def afficher_salaires(request):
   
    salaires = Salaire.objects.all().order_by('-annee', '-moisdetravail')  # Trie par année et mois (descendant)
    
    # Afficher dans un template
    return render(request, 'afficher_salaires.html', {'salaires': salaires})
