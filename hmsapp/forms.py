from django import forms
from .models import Patient, MedicalRecord

class PatientForm(forms.ModelForm):
    class Meta:
       model = Patient
       fields = ['first_name', 'last_name', 'date_of_birth', 'contact_number', 'email', 'blood_group']

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['patient', 'date', 'diagnosis', 'treatment', 'test_results',
                  'doctor_name', 'prescription', 'medical_tests', 'follow_up_instructions', 'symptoms']

class UpdatePatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class DeletePatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = []