from django.urls import path

from . import views

urlpatterns = [
    path('reg_lend', views.reg_lend, name='reg_lend'),
    path('home_lend', views.home_lend, name='home_lend'),
]
