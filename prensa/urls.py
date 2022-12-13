from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('cis.html', views.cis, name='cis'),
    path('fletor.html', views.fletor, name='fletor'),
    path('momFletor', views.momFletor, name='momFletor'),
    path('flex.html', views.flex, name='flex'),
    path('maxFlex', views.maxFlex, name='maxFlex'),
    path('normal.html', views.normal, name='normal'),
    path('tensNormal', views.tensNormal, name='tensNormal'),
    path('cis.html', views.cis, name='cis'),
    path('tensCis', views.tensCis, name='tensCis'),
]