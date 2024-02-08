from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Vehicle, MaintenanceLog

class VehicleListView(ListView):
    model = Vehicle
    template_name = 'vehicle_list.html'
    context_object_name = 'vehicles'

class MaintenanceLogListView(ListView):
    model = MaintenanceLog
    template_name = 'maintenance_log_list.html'
    context_object_name = 'maintenance_logs'

class MaintenanceLogDetailView(DetailView):
    model = MaintenanceLog
    template_name = 'maintenance_log_detail.html'
    context_object_name = 'maintenance_log'
