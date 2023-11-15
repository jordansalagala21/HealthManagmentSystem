
from django.db import models

BLOOD_GROUP_CHOICES = (
    ('A+', 'A+'),
    ('B+', 'B+'),
    ('AB+', 'AB+'),
    ('O+', 'O+'),
    ('A-', 'A-'),
    ('B-', 'B-'),
    ('AB-', 'AB-'),
    ('O-', 'O-'),
)

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=20)
    email = models.EmailField(default='email')
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUP_CHOICES, null=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    test_results = models.TextField()
    doctor_name = models.CharField(max_length=100, blank=True, null=True)
    prescription = models.TextField(blank=True, null=True)
    medical_tests = models.TextField(blank=True, null=True)
    follow_up_instructions = models.TextField(blank=True, null=True)
    symptoms = models.TextField(blank=True, null=True)
