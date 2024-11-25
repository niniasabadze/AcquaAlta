from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Marker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    disruption_type = models.CharField(
        max_length=100,
        null=True,  # Optional
        blank=True  # Allows empty input
    )
    like_count = models.PositiveIntegerField(default=0)
    dislike_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - ({self.latitude}, {self.longitude}) - {self.title}"

class Location(models.Model):
    address = models.CharField(max_length=255)  # Name of the street or location
    city = models.CharField(max_length=100, default="Milan")  # Default to Milan
    latitude = models.FloatField()  # Latitude coordinate
    longitude = models.FloatField()  # Longitude coordinate
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of when the location was added

    def __str__(self):
        return f"{self.address}, {self.city}"
