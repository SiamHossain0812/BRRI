from django.urls import path
from . import views

urlpatterns = [
    path('admin_login/', views.login_page, name='login'),
    path('gw_registration/', views.register_device, name='register_device'),
]