from django.contrib import admin 

from .models import Vehicle, MaintenanceLog 

 

class VehicleAdmin(admin.ModelAdmin): 

    list_display = ('__str__', 'year') 

 

class MaintenanceLogAdmin(admin.ModelAdmin): 

    list_display = ('vehicle', 'formatted_date', 'description', 'cost') 

 

admin.site.register(Vehicle, VehicleAdmin) 

admin.site.register(MaintenanceLog, MaintenanceLogAdmin) 

 

 