from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import  RequestContext
from django.http import HttpResponseRedirect 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate 

from .models import *
from .forms import *
# Create your views here.

# Create your views here.
def index_view(request):
     Numero = Count.objects.get(id=1)
     Numero.contador += 1
     Numero.save()
     return render_to_response('home/index.html', {'Visitors':Numero}, context_instance=RequestContext(request))

def About_view(request):
	return render_to_response('home/About.html', context_instance = RequestContext(request))

def Directorio_view(request):
	return render_to_response('home/Directorio.html', context_instance = RequestContext(request))

def Noticias_view(request):
	Control = Noti.objects.count()
	if Control > 20:
		Ultim = Noti.objects.earliest('id')
		Ultim.delete()
		Notis = Noti.objects.values('user','titulo','cuerpo','fecha', 'hora', 'imagen').order_by("fecha", "hora").reverse()
	else:
		Notis = Noti.objects.values('user','titulo','cuerpo','fecha', 'hora', 'imagen').order_by("fecha", "hora").reverse()
	#.extra(where=['imagen=^$'], params=[''])
	return render_to_response('home/Noticias.html', {'Noticias':Notis}, context_instance = RequestContext(request))

def Login_view(request):
	mensaje = " "
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				user_name = form.cleaned_data['user_name']
				password_user = form.cleaned_data['password_user']
				usuario = authenticate(username = user_name, password = password_user)
			if usuario is not None and usuario.is_active:
				login(request, usuario)
				return HttpResponseRedirect('/')
			else: 
				mensaje = "Usuario y/o Password no son Correctos"
		form=LoginForm()
		ctx = {'form':form, 'mensaje':mensaje}
	return render_to_response('home/Login.html', ctx, context_instance = RequestContext(request))


def Logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required(login_url='/Login')
def Panel_view(request):
	return render_to_response('home/Panel.html', context_instance = RequestContext(request))


@login_required(login_url='/Login')
def PanelNoti_view(request):
	if request.method=='POST':
			formulario = NoticiaForm(request.POST, request.FILES)
			if formulario.is_valid():
				#Captura de los campos del formulario#
				Titulo		= formulario.cleaned_data['titulo']
				Cuerpo		= formulario.cleaned_data['cuerpo']
				Imagen		= formulario.cleaned_data['imagen']
				
				User = request.user.username
				#Registro en el Modelo#
				p		= Noti()
				p.titulo		= Titulo
				p.cuerpo	= Cuerpo
				p.imagen	= Imagen
				p.user = User
				p.save()
				return HttpResponseRedirect('/Noticias')


	else: 
		formulario = NoticiaForm() 
	return render_to_response('home/PanelNoti.html', {'form':formulario},context_instance = RequestContext(request))
# Create your views here.

def Agenda_view(request):
	Notis = Eventos.objects.values('user','titulo','cuerpo','fecha', 'hora', 'imagen').order_by("fecha", "hora")
	return render_to_response('home/Agenda.html', {'Noticias':Notis}, context_instance = RequestContext(request))

@login_required(login_url='/Login')
def PanelEvent_view(request):
	if request.method=='POST':
			formulario = EventosForm(request.POST, request.FILES)
			if formulario.is_valid():
				#Captura de los campos del formulario#
				Titulo		= formulario.cleaned_data['titulo']
				Cuerpo		= formulario.cleaned_data['cuerpo']
				Fecha		= formulario.cleaned_data['fecha']
				Hora		= formulario.cleaned_data['hora']
				Imagen		= formulario.cleaned_data['imagen']
				User = request.user.username
				if Fecha < Fecha.today():
					return HttpResponseRedirect('/Error')
				else:
				#Registro en el Modelo#
					p		= Eventos()
					p.titulo		= Titulo
					p.cuerpo	= Cuerpo
					p.fecha	= Fecha
					p.hora	= Hora
					p.imagen	= Imagen
					p.user = User
					p.save()
					return HttpResponseRedirect('/Agenda')


	else: 
		formulario = EventosForm() 
	return render_to_response('home/PanelEvent.html', {'form':formulario},context_instance = RequestContext(request))

@login_required(login_url='/Login')
def Error_view(request):
	return render_to_response('home/Error.html', context_instance = RequestContext(request))

