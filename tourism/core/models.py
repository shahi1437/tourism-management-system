from django.db import models
from django.contrib.auth.models import User

class Destination(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='destinations/', null=True, blank=True)
    location = models.CharField(max_length=200, default="Unknown")
    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class TravelPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    travel_date = models.DateField()
    destinations = models.ManyToManyField(Destination)

    def __str__(self):
        return f"{self.user.username} Plan ({self.travel_date})"


# ✅ NEW MODEL (Module 3)
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.destination.name}"