from django.urls import path

from . import views

urlpatterns = [
    path('reg_borrow', views.reg_borrow, name='reg_borrow'),
    path('home_borrow', views.home_borrow, name='home_borrow'),
    path('metrics', views.prometheus_metrics, name='prometheus_metrics'),
    path('health', views.health_check, name='health_check'),
]
