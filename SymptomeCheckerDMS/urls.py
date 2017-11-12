from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
    url(r'^symptom$', views.symptom, name='symptom'),
    url(r'^welcome', views.welcome, name='welcome'),
    url(r'^test', views.test, name='test'),
    url(r'^fuckyou', views.fuckyou, name='fuckyou'),
]