# forms.py
from django import forms
from .models import Patient, MedicalRecord, Appointment, Doctor, Billing

class PatientForm(forms.ModelForm):
    class Meta:
       model = Patient
       fields = ['first_name', 'last_name', 'date_of_birth', 'contact_number', 'email', 'blood_group']

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['patient', 'date', 'diagnosis', 'treatment', 'test_results',
                   'prescription', 'medical_tests', 'follow_up_instructions', 'symptoms']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'app_date', 'status']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['doctorId', 'first_name', 'last_name', 'specification', 'contact_number', 'email']


class UpdatePatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class DeletePatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = []

class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['patient', 'billdate', 'total_payment', 'payment_mode', 'insurance']
