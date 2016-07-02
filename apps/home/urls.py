from django.conf.urls import patterns, include, url
from apps.home.views import *

urlpatterns = patterns('apps.home.views',
	
	url(r'^index/$',index_view, name = 'vista_principal'),

	
	url(r'^About/$', About_view, name = 'vista_About'),

	url(r'^Directorio/$', Directorio_view, name = 'vista_Directorio'),

	url(r'^Noticias/$', Noticias_view, name = 'vista_Noticias'),
	
	#Urls de Login y Logout
	url(r'^Login/$',Login_view, name = 'vista_Login'),

	url(r'^Logout/$',Logout_view, name = 'vista_Logout'),

	#Panel
	url(r'^Panel/$',Panel_view, name = 'vista_Panel'),

	url(r'^Agenda/$',Agenda_view, name = 'vista_Agenda'),

	url(r'^PanelNoti/$',PanelNoti_view, name = 'vista_PanelNoti'),

	url(r'^PanelEvent/$',PanelEvent_view, name = 'vista_PanelEvent'),

	url(r'^Error/$',Error_view, name = 'vista_Error'),
	)