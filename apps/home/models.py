from django.db import models
from datetime import datetime  
from django.contrib.auth.models import User



# Create your models here. python manage.py syncdb python manage.py makemigrations python manage.py migrate

class Noti(models.Model):
	titulo = models.CharField(max_length = 100)
	cuerpo = models.TextField()
	fecha = models.DateField(auto_now_add= True, blank = True, null = True)
	hora= models.TimeField(auto_now_add= True, blank = True, null = True)
	imagen = models.ImageField(upload_to='PrimerBiblioteca/media', blank=True, null=True, default='PrimerBiblioteca/media/poke.png')
	#fecha = models.DateTimeField(auto_now_add= True, blank = False)
	user =  models.CharField(max_length = 24)
	def __unicode__(self):
		return str(self.titulo)

class Eventos(models.Model):
	titulo = models.CharField(max_length = 100)
	cuerpo = models.TextField()
	fecha = models.DateField(blank = False, null = False)
	hora= models.TimeField(blank = True, null = True)
	imagen = models.ImageField(upload_to='PrimerBiblioteca/media', blank=True, null=True, default='PrimerBiblioteca/media/poke.png')
	#fecha = models.DateTimeField(auto_now_add= True, blank = False)
	user =  models.CharField(max_length = 24)
	def __unicode__(self):
		return str(self.fecha)

class Count(models.Model):
	contador = models.IntegerField()
	def __unicode__(self):
		return str(self.contador)

