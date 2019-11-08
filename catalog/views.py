from django.shortcuts import render

from django.http import HttpResponse

from .models import ProductionCompany, Producer, Program

# Create your views here.
def catalog(request):
    return HttpResponse("Welcome to the Television System Catalog app!")

def a(request):
    records = ProductionCompany.objects.values()
    context = {'records': records}
    return render(request, 'catalog/productioncompany.html', context)

def b(request):
    records = Producer.objects.values()
    context = {'records': records}
    return render(request, 'catalog/producer.html', context)

def c(request):
    records = Program.objects.values()
    context = {'records': records}
    return render(request, 'catalog/program.html', context)
