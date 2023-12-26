from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404 , redirect
from apps.contacto.forms import ContactoForm
from django.core.paginator import Paginator
from django.http import Http404
from django.urls import reverse
from django.contrib import messages

#Aquí se colocará la parte lógica de la pagina. Acciones de mostrar por pantalla, botones, ciclos, etc.

def INICIO(request):
	return render(request,'HOME.html')

def MOSTRARCONTACTO(request):
	data = {
		"form": ContactoForm()
	}
	if request.method == "POST":
		formulario = ContactoForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			data["mensaje"]="Mensaje Enviado."
		else:
			data["form"] = formulario

	return render(request,'CONTACTO.html', data)


def MOSTRARACERCA(request):
	return render(request,'ACERCA_DE.html')
	

def agregar_post(request):
    return render(request, 'posts/agregar_post.html')
