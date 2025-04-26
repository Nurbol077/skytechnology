from django.db import models
from django.conf import settings  # Для связи с пользователем
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    capacity = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='places')

    def __str__(self):
        return self.name

class TimeSlot(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='timeslots')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.place.name} | {self.date} | {self.start_time}-{self.end_time}"

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    timeslot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('booked', 'Booked'), ('cancelled', 'Cancelled')], default='booked')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Booking by {self.user} for {self.place} on {self.timeslot.date} {self.timeslot.start_time}"


