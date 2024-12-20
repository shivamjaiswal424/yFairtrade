"""FairTrade URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:

Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views
from Borrower.views import prometheus_metrics

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Auth.urls')),
    path('about', views.about, name='about'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('lend/', include('Lender.urls')),
    path('borrow/', include('Borrower.urls')),
    path('metrics', prometheus_metrics, name='prometheus_metrics'),
]
