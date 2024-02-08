from django.test import TestCase
from django.urls import reverse
from .models import Vehicle, MaintenanceLog

class VehicleMaintenanceTestCase(TestCase):
    def setUp(self):
        # Create a sample vehicle
        self.vehicle = Vehicle.objects.create(make="Toyota", model="Camry", year=2022)

    def test_vehicle_list_view(self):
        # Test the vehicle list view
        response = self.client.get(reverse("vehicle-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Toyota Camry (2022)")

    def test_maintenance_log_list_view(self):
        # Test the maintenance log list view
        MaintenanceLog.objects.create(
            vehicle=self.vehicle,
            date="2023-01-01",
            description="Oil Change",
            cost=50.00,
            receipt="path/to/receipt.jpg",
        )
        response = self.client.get(reverse("maintenance-log-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Toyota Camry (2022)")
        self.assertContains(response, "Oil Change")
        self.assertContains(response, "January 01, 2023")

    def test_maintenance_log_detail_view(self):
        # Test the maintenance log detail view
        maintenance_log = MaintenanceLog.objects.create(
            vehicle=self.vehicle,
            date="2023-01-11",
            description="Oil Change",
            cost=50.00,
            receipt="path/to/receipt.jpg",
        )
        response = self.client.get(reverse("maintenance-log-detail", args=[maintenance_log.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Toyota Camry (2022)")
        self.assertContains(response, "Oil Change")
        self.assertContains(response, "January 11, 2023")
        self.assertContains(response, "Cost: $50.00")

    # Add more test cases as needed
