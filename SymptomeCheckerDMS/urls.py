from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^symptomdemo$', views.symptom, name='symptom'),
    url(r'^register',views.register,name='register'),
    url(r'^about',views.about,name='about'),
    url(r'^testbootstrap',views.testbootstrap,name='testbootstrap'),
    url(r'^getwidget',views.compute),
]