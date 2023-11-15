from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient, MedicalRecord
from .forms import PatientForm, MedicalRecordForm

def home(request):
    # Your view logic here
    return render(request, 'hmsapp/home.html')

def add_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_patients')  # Redirect to the same page after adding a patient
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
    print(patients) 
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
    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == "POST":
        confirmed = request.POST.get('confirmed', False)
        if confirmed:
            patient.delete()
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
            # Redirect to the view_medical_records page for the associated patient
            return redirect('view_medical_records', patient_id=record.patient.id)
    else:
        form = MedicalRecordForm(instance=record)

    return render(request, 'hmsapp/update_medical_record.html', {'form': form})