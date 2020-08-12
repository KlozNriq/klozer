from django.shortcuts import render

# Create your views here.
# (vista nueva)
def index(request):
    return render(request, 'main/index.html',{
        'title': 'Inicio'
    })

def about(request):
    return render(request, 'main/about.html',{
        'title': 'Nosotros'
    })

def services(request):
    return render(request, 'main/services.html',{
        'title': 'Servicios'
    })

def projects(request):
    return render(request, 'main/projects.html',{
        'title': 'Proyectos'
    })

def contact(request):
    return render(request, 'main/contact.html',{
        'title': 'Contacto'
    })