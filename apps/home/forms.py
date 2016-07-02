from django import forms
from django.forms import ModelForm
from .models import *
from PIL import Image
from django.forms import extras


#Importar
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#Este es el formulario de Login
class LoginForm(forms.Form):
		user_name = forms.CharField(widget = forms.TextInput())
		password_user = forms.CharField(widget = forms.PasswordInput(render_value = False))

#Noticias
class NoticiaForm(forms.Form):
	titulo = forms.CharField(widget = forms.TextInput(), initial='Escribe aqui tu titulo')
	cuerpo = forms.CharField(widget=forms.Textarea, initial='Escribe aqui el cuerpo de tu noticia')
	imagen = forms.ImageField(label='Selecciona un archivo', required = False)
	#user =  forms.CharField(widget = forms.TextInput())

#Eventos
class EventosForm(forms.Form):
	titulo = forms.CharField(widget = forms.TextInput(), initial='Escribe aqui tu titulo')
	cuerpo = forms.CharField(widget=forms.Textarea, initial='Escribe aqui el cuerpo de tu noticia')
	fecha = forms.DateField (widget=extras.SelectDateWidget)
	hora = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), initial='Ejemplo 14:25')
	#hora = forms.TimeField(widget=extras.SelectTimeWidget)
	imagen = forms.ImageField(label='Selecciona un archivo', required = False)
	#user =  forms.CharField(widget = forms.TextInput())


