from django.urls import path
from . import views


urlpatterns = [
    path('create', views.new_url, name='main'),
    path('personal_account_front', views.view_urls, name='dashboard'),
    path('personal_account_server', views.view_urls_server.as_view(), name='dashboard_server'),
    path('personal_account_server_json', views.view_urls_server_json.as_view(), name='dashboard_server_json'),
    path('<str:url_short>/edit/', views.edit_url, name='link_edit'),
    path('<str:url_short>/delete/', views.delete_url, name='link_delete'),
    path('<str:url_short>', views.show_urls, name='link'),

]
