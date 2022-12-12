from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('cis.html', views.cis, name='cis'),
    path('fletor.html', views.fletor, name='fletor'),
    path('flex.html', views.flex, name='flex'),
    path('normal.html', views.normal, name='normal'),
]