from django.db import models 

 

class Vehicle(models.Model): 

    make = models.CharField(max_length=50) 

    model = models.CharField(max_length=50) 

    year = models.IntegerField() 

 

    def __str__(self): 

        return f"{self.make} {self.model} ({self.year})" 

 

class MaintenanceLog(models.Model): 

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE) 

    date = models.DateField() 

    description = models.TextField() 

    cost = models.DecimalField(max_digits=8, decimal_places=2) 

    receipt = models.ImageField(upload_to='maintenance_receipts/', blank=True, null=True) 

 

    def formatted_date(self): 

        return self.date.strftime("%B %d, %Y") 

 

    def __str__(self): 

        return f"{self.vehicle} - {self.formatted_date()}" 