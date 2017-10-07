from django.conf.urls import url
from . import views    

urlpatterns = [
	url(r'^$', views.index),
	url(r'index$', views.index),
	url(r'^process_money$', views.process_money),
	url(r'^clear$', views.reset)
  ]
  