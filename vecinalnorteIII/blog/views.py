from django.shortcuts import render
from .models import Material_mediomenor, Material_cuentos, Material_mediomayor, Material_medios, Material_salacuna
# Create your views here.

def home(request):
    return render(request,'index.html')


def nuestrojardin(request):
    return render(request, 'nuestrojardin.html')

def familinea(request):
    return render(request, 'familinea.html')

def recursos(request):
    return render(request, 'recursos.html')



def mediomenor(request):
    Material_mediomenor_list= Material_mediomenor.objects.all()
    context={
        'Material_mediomenor_list': Material_mediomenor_list,
    }
    return(render(request, 'mediomenor.html', context))

def mediomayor(request):
    Material_mediomayor_list= Material_mediomayor.objects.all()
    context={
        'Material_mediomayor_list': Material_mediomayor_list,
    }
    return(render(request, 'mediomayor.html', context))

def medios(request):
    Material_medios_list= Material_medios.objects.all()
    context={
        'Material_medios_list': Material_medios_list,
    }
    return(render(request, 'medios.html', context))

def salacuna(request):
    Material_salacuna_list= Material_salacuna.objects.all()
    context={
        'Material_salacuna_list': Material_salacuna_list,
    }
    return(render(request, 'salacuna.html', context))

def cuentos(request):
    Material_cuentos_list= Material_cuentos.objects.all()
    context={
        'Material_cuentos_list': Material_cuentos_list,
    }
    return(render(request, 'cuentos.html', context))




