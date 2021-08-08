from django.shortcuts import render,get_object_or_404,redirect
from .models import Doctor,department

# Create your views here.
def departfun(request,d_slug=None):
    d_page=None
    doc=None
    if d_slug!=None:

        d_page=get_object_or_404(department,slug=d_slug)
        doc=Doctor.objects.filter(depart=d_page, available=True)
    else:
        doc=Doctor.objects.all().filter(available=True)
    dep=department.objects.all()

    return render(request,"index.html",{'doc':doc,'dep':dep})

def doctfunc(request,d_slug,doc_slug):
    try:
     docto=Doctor.objects.get(depart__slug=d_slug,slug=doc_slug)
    except Exception as e:
        raise e
    return render(request,"item.html",{"doc":docto})

