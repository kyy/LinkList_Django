"""djangoLnkList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path
from . import views


urlpatterns = [
path('', views.new_url, name='main'),
path('dashboard', views.view_urls, name='dashboard'),
path('<str:url_short>/edit/', views.edit_url, name='link_edit'),
path('<str:url_short>/delete/', views.delete_url, name='link_delete'),
path('<str:url_short>', views.show_urls, name='link'),

]