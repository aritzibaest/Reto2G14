from django.shortcuts import render
from .models import Departamento,Habilidad,Empleado

# Create your views here.
from django.http import HttpResponse

def index(request):
    departamentos = Departamento.objects.order_by('nombre')
    context = {'titulo_pagina':'Lisado de departamentos','lista_departamentos' : departamentos}
    return render(request, 'departamentos.html', context)

def departamento(request, departamento_id):
    departamento = Departamento.objects.get(pk=departamento_id)
    return HttpResponse(departamento)

def empleado(request, empleado_id):
    empleado = Empleado.objects.get(pk=empleado_id)
    context = {'titulo_pagina': 'Detalles de empleado', 'empleado': empleado}
    return render(request, 'empleados.html', context)
