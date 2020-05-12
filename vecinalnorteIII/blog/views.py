from django.shortcuts import render
from .models import Material_mediomenor
# Create your views here.

def home(request):
    return render(request,'index.html')

def material(request):
    Material_mediomenor_list= Material_mediomenor.objects.all()
    context={
        'Material_mediomenor_list': Material_mediomenor_list,
    }
    return(render(request, 'post.html', context))
