from django.db import models
from django.utils import timezone
from accounts.models import Account
from pets.models import Pet
# Create your models here.

class Appointments(models.Model):
    customer = models.ForeignKey(
        Account,
        on_delete=models.CASCADE
    )

    pet = models.ForeignKey (
        Pet, 
        on_delete=models.CASCADE
    )

    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=200)

    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['start_time']
        verbose_name_plural = "Appointments"

    def __str__(self):
        return f'{self.customer} appointment at {self.location}'