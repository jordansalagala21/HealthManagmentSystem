
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

class Doctor(models.Model):
    doctorId = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specification = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} ({self.specification})"

class Appointment(models.Model):
    appID = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    app_date = models.DateTimeField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Appointment {self.appID} with {self.patient.first_name} {self.patient.last_name} on {self.app_date}"