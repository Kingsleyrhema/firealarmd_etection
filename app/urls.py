from django.urls import path
from . import views

urlpatterns = [
    path('device_dashboard', views.device_dashboard, name='device_dashboard'),
    path('', views.about, name='about'),
    path('contact us', views.contact, name='contact'),
    path('get-sensor-data/', views.get_sensor_data, name='get_sensor_data'),
    path('update-alarm-status/', views.update_alarm_status, name='update_alarm_status'),
]