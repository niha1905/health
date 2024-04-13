#views.py
from django.shortcuts import render
from django.views.generic import ListView
import csv
#from airtable import Airtable
from .models import PatientRecord

'''# Replace these with your Airtable API key, base ID, and table name
AIRTABLE_API_KEY = 'pat7hpgmy2itPqWrX.da8a874efe149fc7f8569d6297d44973b6175731bb489123aa14de17b35686ae'
AIRTABLE_BASE_ID = 'app2WlcjTHxf5aCIZ'
AIRTABLE_TABLE_NAME = 'smartwatch_data'

# Create an Airtable object
airtable = Airtable(AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME, AIRTABLE_API_KEY)
'''

def home(request):
    return render(request, 'admin_page/admin.html')

def about(request):
    return render(request, 'admin_page/about.html')

def patients(request):
    return render(request, 'admin_page/patients.html')

def skinTemp(request):
    return render(request, 'admin_page/skin_temperature_link.html')

def stepCount(request):
    return render(request, 'admin_page/step_counter_link.html')

def bp(request):
    return render(request, 'admin_page/blood_pressure_link.html')

def heartRate(request):
    return render(request, 'admin_page/heart_rate_link.html')

def oxSat(request):
    return render(request, 'admin_page/oxygen_saturation_link.html')

def pulse(request):
    return render(request, 'admin_page/pulse_link.html')



# views.py

'''from django.shortcuts import render
from .onesignal_utils import send_push_notification

def my_view(request):
    player_ids = ['player_id_1', 'player_id_2']  # Replace with recipient's player IDs
    message = 'Hello from Django!'  # Your push notification message
    send_push_notification(player_ids, message)

'''