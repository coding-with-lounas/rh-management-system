from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('candidature/', views.candidat_create_view, name='candidat_create'),
    path('candidature/success/',views.candidat_success_view, name='candidat_success'),
]
