from django.shortcuts import render,redirect,get_object_or_404
from .models import Employe,Service,Absence,Massrouf,Contrat,Salaire,Recrutement
from .forms import EmployeForm,ServiceForm,AbsenceForm ,MassroufForm,RecrutementForm,CustomUserCreationForm,ContratForm,RechercheContratForm
from django.contrib import messages
from django.db.models import Q,Count,Sum
from datetime import datetime,timedelta, date
from django.db.models.signals import post_save
from django.dispatch import receiver
from dateutil.relativedelta import relativedelta 
from django.db.models.functions import TruncMonth
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import io
from django.template.loader import render_to_string
from xhtml2pdf import pisa


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

 

# Afficher la liste des recrutements
def afficherRecrutements(request):
    recrutements = Recrutement.objects.all()
    return render(request, 'liste_recrutements.html', {'recrutements': recrutements, 'search_mode': False})

# Ajouter un recrutement
def ajouterRecrutement(request):
    if request.method == 'POST':
        form = RecrutementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Le recrutement a été ajouté avec succès.")
            return redirect('listeRecrutements')  # Redirige vers la liste des recrutements
        else:
            messages.error(request, "Erreur : Veuillez corriger les erreurs dans le formulaire.")
    else:
        form = RecrutementForm()
    return render(request, 'ajouter_recrutement.html', {'form': form})

# Modifier un recrutement
def editerRecrutement(request, pk):
    recrutement = get_object_or_404(Recrutement, pk=pk)
    if request.method == 'POST':
        form = RecrutementForm(request.POST, instance=recrutement)
        if form.is_valid():
            form.save()
            messages.success(request, "Le recrutement a été modifié avec succès.")
            return redirect('listeRecrutements')  # Redirige vers la liste des recrutements
        else:
            messages.error(request, "Erreur : Veuillez corriger les erreurs dans le formulaire.")
    else:
        form = RecrutementForm(instance=recrutement)
    return render(request, 'editer_recrutement.html', {'form': form, 'recrutement': recrutement})

def supprimerRecrutement(request, pk):
    recrutement = get_object_or_404(Recrutement, pk=pk)
    if request.method == 'POST':
        try:
            recrutement.delete()
            messages.success(request, "Le recrutement a été supprimé avec succès.")
        except Exception as e:
            messages.error(request, f"Erreur lors de la suppression : {str(e)}")
        return redirect('listeRecrutements')  # Redirige vers la liste des recrutements
    return render(request, 'supprimer_recrutement.html', {'recrutement': recrutement})

# Rechercher des recrutements
def rechercherRecrutements(request):
    query = request.GET.get('search', '')  # Récupère le terme de recherche
    recrutements = Recrutement.objects.all()  # Récupère tous les recrutements par défaut

    if query:  # Si un terme de recherche est présent
        recrutements = recrutements.filter(
            poste__icontains=query
        ) | recrutements.filter(
            statut__icontains=query
        )
        if not recrutements.exists():  # Si aucun résultat trouvé
            message = "Aucun recrutement ne correspond à votre recherche."
            return render(request, 'liste_recrutements.html', {'recrutements': Recrutement.objects.all(), 'message': message, 'search_mode': True})
    
    return render(request, 'liste_recrutements.html', {'recrutements': recrutements, 'search_mode': True})

# Liste des contrats avec recherche
def liste_contrats(request):
    contrats = Contrat.objects.all()
    form = RechercheContratForm(request.GET)
    
    if form.is_valid():
        search = form.cleaned_data.get('search')
        if search:
            contrats = contrats.filter(type_contrat__icontains=search)
    
    context = {
        'Contrats': contrats,
        'form': form,
    }
    return render(request, 'contrats_list.html', context)

# Ajouter un contrat
def ajouter_contrat(request):
    if request.method == 'POST':
        form = ContratForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contratList')  # redirige vers la liste des contrats
    else:
        form = ContratForm()
    
    context = {
        'form': form
    }
    return render(request, 'add_contrat.html', context)

# Modifier un contrat
def modifier_contrat(request, contrat_id):
    contrat = get_object_or_404(Contrat, id=contrat_id)
    if request.method == 'POST':
        form = ContratForm(request.POST, instance=contrat)
        if form.is_valid():
            form.save()
            return redirect('contratList')
    else:
        form = ContratForm(instance=contrat)
    
    context = {
        'form': form,
        'contrat': contrat
    }
    return render(request, 'edit_contrat.html', context)

# Supprimer un contrat
def supprimer_contrat(request, contrat_id):
    contrat = get_object_or_404(Contrat, id=contrat_id)
    if request.method == 'POST':
        contrat.delete()
        return redirect('contratList')
    
    context = {
        'contrat': contrat
    }
    return render(request, 'delete_contrat.html', context)

def imprimer_contrat(request, contrat_id):
    # Récupérer le contrat à imprimer
    contrat = Contrat.objects.get(id=contrat_id)
    
    # Créer un contexte de données à passer à votre template
    context = {
        'contrat': contrat,
    }
    
    # Charger le template HTML pour le contrat
    template = 'contrat_template.html'  # Votre template HTML pour le contrat
    
    # Rendre le template avec le contexte
    html_content = render_to_string(template, context)
    
    # Créer une réponse HTTP avec le contenu PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="contrat_{contrat.id}.pdf"'
    
    # Utiliser xhtml2pdf pour convertir le HTML en PDF
    pisa_status = pisa.CreatePDF(html_content, dest=response)
    
    # Vérifier si le PDF a été créé avec succès
    if pisa_status.err:
        return HttpResponse('Erreur lors de la génération du PDF', status=500)
    
    return response

def analyse_absences(request):
    # Regrouper les absences par mois et compter les occurrences
    absences_par_mois = (
        Absence.objects.annotate(month=TruncMonth('date_Absence'))
        .values('month')
        .annotate(total=Count('id'))
        .order_by('month')
    )
    
    # Convertir les données en format utilisable par JavaScript dans le template
    data = {
        'labels': [item['month'].strftime('%Y-%m') for item in absences_par_mois],
        'data': [item['total'] for item in absences_par_mois],
    }
    
    # Rendre le template avec les données
    return render(request, 'analyse_absences.html', {'data': data})

def analyseActivite(request):
    today = date.today()
  
    # Récupérer tous les employés
    employees = Employe.objects.all()
    
    # Statistiques par Sexe
    sexe_stats = employees.values('sexe').annotate(count=Count('id'))
    sexe_counts = {'M': 0, 'F': 0}
    for stat in sexe_stats:
        sexe_counts[stat['sexe']] = stat['count']

    # Calculer l'Age et l'Ancienneté
    seniority_counts = {0: 0, 1: 0, 2: 0, 3: 0}  # Divise par année (0-1, 1-2, etc)
    for emp in employees:
        # Calcul de l'âge
        age = today.year - emp.date_naissance.year - ((today.month, today.day) < (emp.date_naissance.month, emp.date_naissance.day))
        
        # Calcul de l'ancienneté
        seniority = today.year - emp.date_embauche.year - ((today.month, today.day) < (emp.date_embauche.month, emp.date_embauche.day))
        
        # Classification de l'ancienneté
        if seniority <= 1:
            seniority_counts[0] += 1
        elif seniority <= 2:
            seniority_counts[1] += 1
        elif seniority <= 3:
            seniority_counts[2] += 1
        else:
            seniority_counts[3] += 1

    # Rendre les données à la page pour Chart.js
    return render(request, 'analyseActivite.html', {
        'sexe_counts': sexe_counts,
        'seniority_counts': seniority_counts,
    })


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




# Create your views here.
def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('empList')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'connexion.html')

@login_required
def acceuil(request):
    return render(request, 'acceuil.html')

def deconnexion(request):
    logout(request)
    return redirect('connexion')
