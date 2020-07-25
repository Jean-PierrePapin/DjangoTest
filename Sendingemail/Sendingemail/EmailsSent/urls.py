from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sendingemails/', views.sendingemails, name='sendingemails')
]
