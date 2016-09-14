from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^Celula/(?P<slug_celula>[-\w]+)/$', views.DetailCelulaListRedesLan.as_view(), name="detailCelulaAndListRedesLan"),
	url(r'^linea/(?P<slug_linea>[-\w]+)/$', views.DetailLineaAndListCelulas.as_view(), name="detailLineaAndlistCelulas"),
 	url(r'^lineas', views.ListLineas.as_view(),name="listLineas"),
]