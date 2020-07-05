from django.shortcuts import render
from aulas.models import Aulas
# Create your views here.


def listAulas(request):
    return render(request=request,
                  template_name="list_aulas.html",
                  context={"listAulas": Aulas.objects.all})


def base(request):
    return render(request=request,
                  template_name="base.html")
