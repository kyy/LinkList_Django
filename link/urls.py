from django.urls import path
from . import views


urlpatterns = [
                path('', views.new_url, name='main'),
                path('dashboard', views.view_urls, name='dashboard'),
                path('<str:url_short>/edit/', views.edit_url, name='link_edit'),
                path('<str:url_short>/delete/', views.delete_url, name='link_delete'),
                path('<str:url_short>', views.show_urls, name='link'),
]
