from django.contrib import admin
from django.urls import path
from app_i.views import VehicleListView, MaintenanceLogListView, MaintenanceLogDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehicles/', VehicleListView.as_view(), name='vehicle-list'),
    path('maintenance-logs/', MaintenanceLogListView.as_view(), name='maintenance-log-list'),
    path('maintenance-logs/<int:pk>/', MaintenanceLogDetailView.as_view(), name='maintenance-log-detail'),
]
