from django.urls import path, include, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'urls', views.AlbumViewSet)

urlpatterns = [
    path('create', views.new_url, name='main'),
    path('personal_account_front', views.view_urls, name='dashboard'),
    re_path('^api/', include(router.urls)),
    path('personal_account_server', views.view_urls_server, name='dashboard_server'),
    path('<str:url_short>/edit/', views.edit_url, name='link_edit'),
    path('<str:url_short>/delete/', views.delete_url, name='link_delete'),
    path('<str:url_short>', views.show_urls, name='link'),

]
