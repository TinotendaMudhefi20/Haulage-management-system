from django.db import models

# Create your models here.
from django.db import models
from trucks.models import Truck
from drivers.models import Driver

class Job(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]

    pickup_location = models.CharField(max_length=255)
    delivery_location = models.CharField(max_length=255)
    cargo_description = models.TextField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return f"Job {self.id}"