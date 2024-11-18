import firebase_admin
from firebase_admin import credentials, db
from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache
import json
import os
from firebase_admin import credentials

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current file
cred = credentials.Certificate(os.path.join(BASE_DIR, "csc242project-f0daf-firebase-adminsdk-5fhxf-f43af4bd80.json"))

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://csc242project-f0daf-default-rtdb.firebaseio.com/'  # Replace with your database URL
})

def device_dashboard(request):
    return render(request, 'app/device.html')

def about(request):
    return render(request, 'app/about.html')

def contact(request):
    return render(request, 'app/contact.html')

def get_sensor_data(request):
    # Check if the sensor data is cached
    sensor_data = cache.get('sensor_data')

    if not sensor_data:
        # If not cached, fetch from Firebase
        ref = db.reference('sensorData')
        sensor_data = ref.get()

        # Fetch alarm status
        alarm_ref = db.reference('alarmStatus')
        alarm_status = alarm_ref.get()

        # If no data, return default
        if not sensor_data:
            sensor_data = {
                'temperature': 'N/A',
                'humidity': 'N/A',
                'mq2Analog': 'N/A',
                'mq2Digital': 'N/A',
            }

        # Cache the sensor data for 10 seconds
        cache.set('sensor_data', sensor_data, timeout=10)

    return JsonResponse(sensor_data)

def update_alarm_status(request):
    status = request.GET.get('status')  # "0" for On, "1" for Off
    if status in ["0", "1"]:
        sensor_data_ref = db.reference('sensorData')
        sensor_data_ref.update({'alarmStatus': int(status)})
        return JsonResponse({'success': True, 'alarmStatus': int(status)})

    return JsonResponse({'success': False, 'message': 'Invalid status'})

