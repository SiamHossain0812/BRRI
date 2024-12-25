from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('admin-registration/', views.admin_registration, name='admin_registration'),  # Fixed consistency here
    path('uao-registration/', views.uao_registration, name='uao_registration'),  # Consistency
    path('saao-registration/', views.saao_registration, name='saao_registration'),  # Consistency
    path('farmer-registration/', views.farmer_registration, name='farmer_registration'),
    path('potentiometer-data/', views.potentiometer_data, name='potentiometer_data'),
    path('laser-data/', views.laser_data, name='laser_data'),
    path('sonar-data/', views.sonar_data, name='sonar_data'),
    path('water-requirement/', views.water_requirement, name='water_requirement'),
    path('irrigation-status/', views.irrigation_status, name='irrigation_status'),
    path('send-feedback/', views.send_feedback, name='send_feedback'),
    path('user-feedbacks/', views.user_feedbacks, name='user_feedbacks'),
]
