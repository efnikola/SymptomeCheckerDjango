from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
    url(r'^symptom$', views.symptom, name='symptom'),
    url(r'^AdditionalQ', views.AdditionalQ, name='AdditionalQ'),
    url(r'^start', views.start, name='start'),
    url(r'^results', views.results, name='results'),
]