from django.db import models
from django.contrib.auth.models import User

from map.models import Marker

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=255, blank=True, null=True, default='Standard')
    
    @property
    def points(self):
        from django.db.models import Sum
        markers = Marker.objects.filter(user=self.user)
        likes = markers.aggregate(Sum('like_count'))['like_count__sum'] or 0
        dislikes = markers.aggregate(Sum('dislike_count'))['dislike_count__sum'] or 0
        return likes - dislikes

    def __str__(self):
        return f"{self.user.username}'s Profile"

