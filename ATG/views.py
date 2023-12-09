from django.contrib import messages
from .models import *
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'frontend/login.html')

def register_page(request):

    if request.method == "POST":
        role = request.POST.get('role')  

        if role == 'doctor':
            # Registration for Doctor
            password=request.POST.get('password'),
            confirm_password=request.POST.get('confirm_password'),
            if(confirm_password==password):
                data = Doctor(
                    first_name=request.POST.get('first_name'),
                    last_name=request.POST.get('last_name'),
                    username=request.POST.get('username'),
                    email=request.POST.get('email'),
                    password=request.POST.get('password'),
                    line1_address=request.POST.get('line1_address'),
                    city=request.POST.get('city'),
                    state=request.POST.get('state'),
                    pincode=request.POST.get('pincode'),
                )
                data.save()
                messages.success(request, "Doctor registration successful")
                return redirect('/login/')
            else:
                messages.success(request, "Password Mismatch!")
                return redirect('/register/')

        elif role == 'patient':
            # Registration for Patient
            password=request.POST.get('password'),
            confirm_password=request.POST.get('confirm_password'),
            if(confirm_password==password):
                data = Patient(
                    first_name=request.POST.get('first_name'),
                    last_name=request.POST.get('last_name'),
                    username=request.POST.get('username'),
                    email=request.POST.get('email'),
                    password=request.POST.get('password'),
                    line1_address=request.POST.get('line1_address'),
                    city=request.POST.get('city'),
                    state=request.POST.get('state'),
                    pincode=request.POST.get('pincode'),
                )
                data.save()
                messages.success(request, "Patient registration successful")
                return redirect('/login/')
            else: 
                messages.success(request, "Password Mismatch!")
                return redirect('/register/')
        else:
            # Invalid role
            messages.error(request, "Invalid role selected")
            return redirect('/register/')

    return render(request, 'frontend/register.html')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the provided username and password are valid for a Doctor
        doctor = Doctor.objects.filter(username=username, password=password).first()

        # Check if the provided username and password are valid for a Patient
        patient = Patient.objects.filter(username=username, password=password).first()

        if doctor:
            # Authentication successful for Doctor
            messages.success(request, "Doctor login successful")
            return redirect('/doctor_dashboard/')  # Redirect to the doctor's dashboard

        elif patient:
            # Authentication successful for Patient
            messages.success(request, "Patient login successful")
            return redirect('/patient_dashboard/')  # Redirect to the patient's dashboard

        else:
            # Authentication failed
            messages.error(request, "Invalid username or password")
            return redirect('/login/')

    return render(request, 'frontend/login.html')



def doctor_dashboard(request):
        doctor_data = Doctor.objects.all()
        return render(request, 'frontend/doctor_dashboard.html', {'doctor_data': doctor_data})
    

def patient_dashboard(request):
        patient_data = Patient.objects.all()
        return render(request, 'frontend/patient_dashboard.html', {'patient_data': patient_data})
    
    