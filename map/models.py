from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Marker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    disruption_type = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    like_count = models.PositiveIntegerField(default=0)
    dislike_count = models.PositiveIntegerField(default=0)
    raindrop_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - ({self.latitude}, {self.longitude}) - {self.title}"

class Location(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100, default="Milan")
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.address}, {self.city}"
