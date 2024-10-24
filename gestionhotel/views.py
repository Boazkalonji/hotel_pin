from django.shortcuts import render,render




def index(request):

    return render(request, 'gestionhotel/index.html')


def about(request):

    return render(request, 'gestionhotel/about.html')


def galerie(request):

    return render(request, 'gestionhotel/galerie.html')


def album1(request):

    return render(request, 'gestionhotel/album1.html')



def album2(request):

    return render(request, 'gestionhotel/album2.html')



def contact(request):

    return render(request, 'gestionhotel/contact.html')


