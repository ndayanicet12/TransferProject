from django.shortcuts import render,RequestContext
from django.contrib.auth import authenticate, login ,logout
from django.core.urlresolvers import reverse
from .forms import ConnexionForm
from django.template import RequestContext
#include('forms.py')


def connexion(request):
    #context = RequestContext(request)

    error = False
    if request.method == "POST":

        form = ConnexionForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["username"]
            mdp = form.cleaned_data["password"]
            user = authenticate(username=name, password=mdp) 
            login(request, user)  # nous connectons l'utilisateur

    else:
        form = ConnexionForm()

    return render(request, 'accounts/connexion.html', context_instance=RequestContext(request))


def deconnexion(request):
    logout(request)
    return redirect(reverse('connexion'))
