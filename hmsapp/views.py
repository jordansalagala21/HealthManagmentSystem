from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient, MedicalRecord, Appointment, Doctor
from .forms import PatientForm, MedicalRecordForm, AppointmentForm, DoctorForm, BillingForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    # Your view logic here
    return render(request, 'hmsapp/home.html')

def add_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)    
        if form.is_valid():
            form.save()
            return redirect('view_patients')  # Redirect to the view patients page
    else:
        form = PatientForm()
    return render(request, 'hmsapp/add_patient.html', {'form': form})

def add_medical_record(request):
    if request.method == "POST":
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_medical_record')  # Redirect to the same page after adding a medical record
    else:
        form = MedicalRecordForm()
    return render(request, 'hmsapp/add_medical_record.html', {'form': form})

def view_patients(request):
    patients = Patient.objects.all()
    return render(request, 'hmsapp/view_patients.html', {'patients': patients})

def update_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('view_patients')
    else:
        form = PatientForm(instance=patient)

    return render(request, 'hmsapp/update_patient.html', {'form': form})

def delete_patient(request, patient_id):
    print("Delete Patient View Reached")
    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == 'POST':
        print("POST request received")
        patient.delete()
        print("Patient deleted")
        return redirect('view_patients')

    return render(request, 'hmsapp/delete_patient.html', {'patient': patient})


def view_medical_records(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    medical_records = MedicalRecord.objects.filter(patient=patient)
    return render(request, 'hmsapp/view_medical_records.html', {'patient': patient, 'medical_records': medical_records})

def update_medical_record(request, record_id):
    record = get_object_or_404(MedicalRecord, id=record_id)

    if request.method == "POST":
        form = MedicalRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('view_medical_records', patient_id=record.patient.id)
    else:
        form = MedicalRecordForm(instance=record)

    return render(request, 'hmsapp/update_medical_record.html', {'form': form})

# Add this import at the top of your views.py
from django.http import HttpResponseRedirect

# Existing views...

def add_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            patient_id = appointment.patient.id if appointment.patient else None
            appointment.save()
            
            # Redirect to the billing page with the patient ID
            billing_url = reverse('billing', kwargs={'patient_id': patient_id})
            return HttpResponseRedirect(billing_url)
    else:
        form = AppointmentForm()

    return render(request, 'hmsapp/add_appointment.html', {'form': form})


def view_appointments(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    appointments = Appointment.objects.filter(patient=patient)
    print(appointments)
    return render(request, 'hmsapp/view_appointments.html', {'patient': patient, 'appointments': appointments})

def update_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            if appointment.patient:
                return redirect('view_appointments', patient_id=appointment.patient.id)
            else:
                return redirect('view_appointments')  # Redirect without patient_id
    else:
        form = AppointmentForm(instance=appointment)

    return render(request, 'hmsapp/update_appointment.html', {'form': form})

def add_doctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_doctors')  # Redirect to the view doctors page after adding a doctor
    else:
        form = DoctorForm()

    return render(request, 'hmsapp/add_doctor.html', {'form': form})

# your existing imports

def billing(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    # Your billing view logic here
    
    return render(request, 'hmsapp/billing.html', {'patient': patient})
