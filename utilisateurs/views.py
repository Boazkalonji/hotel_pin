from django.shortcuts import render
from django.shortcuts import redirect
from  django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm


def login_users(request):

    if request.method == 'POST':
        nom = request.POST['nom']
        mdp = request.POST['mdp']

        user = authenticate(request, username = nom, password = mdp)

        if user is not None:
            return redirect('gestionhotel:index')
        else:
           return render(request,'utilisateurs/erreur.html') 
        
    return render(request,'utilisateurs/login.html') 



def update_user(request):
    
    return render(request,'utilisateurs/update_user.html')


def sing_up(request):

    if request.method == 'POST':

        nom = request.POST['nom']
        mdp = request.POST['mdp']
        postnom = request.POST['postnom']
        prenom = request.POST['prenom']
        email = request.POST['email']


        if nom =='' or mdp =='' or postnom == '' or prenom == '' or email == '':
            return render(request,'utilisateurs/erreur.html')
        else:
            user = User.objects.create_user(username=nom, password=mdp)
            user.first_name = postnom
            user.last_name = prenom
            user.email = email

            user.save()

            return render(request,'utilisateurs/login.html')
    else:
        return render(request,'utilisateurs/sing_up.html')









def reservation(request):
    
    return render(request,'utilisateurs/reservation.html')
