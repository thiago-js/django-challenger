from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'webapp'

urlpatterns = [
    # Inclui as URLs do app ‘website’
    path('maratona', views.listAulas, name="maratona"),
    path('', views.base, name="initial page"),
]
