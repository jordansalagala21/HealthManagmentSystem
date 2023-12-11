# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('add_medical_record/', views.add_medical_record, name='add_medical_record'),
    path('view_patients/', views.view_patients, name='view_patients'),
    path('update_patient/<int:patient_id>/', views.update_patient, name='update_patient'),
    path('delete_patient/<int:patient_id>/', views.delete_patient, name='delete_patient'),
    path('view_medical_records/<int:patient_id>/', views.view_medical_records, name='view_medical_records'),
    path('update_medical_record/<int:record_id>/', views.update_medical_record, name='update_medical_record'),
    path('add_appointment/', views.add_appointment, name='add_appointment'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('view_appointments/<int:patient_id>/', views.view_appointments, name='view_appointments'),
    path('update_appointment/<int:appointment_id>/', views.update_appointment, name='update_appointment'),  
    path('billing/<int:patient_id>/', views.billing, name='billing'),
]
