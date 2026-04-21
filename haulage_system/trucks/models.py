from django.db import models

# Create your models here.
from django.db import models

class Truck(models.Model):
    STATUS_CHOICES = [
        ('AVAILABLE', 'Available'),
        ('IN_TRANSIT', 'In Transit'),
        ('MAINTENANCE', 'Maintenance'),
    ]

    registration_number = models.CharField(max_length=50, unique=True)
    capacity = models.FloatField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='AVAILABLE')

    def __str__(self):
        return self.registration_number
    


   



