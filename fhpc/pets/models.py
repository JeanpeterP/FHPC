from django.db import models,IntegrityError
from accounts.models import Account
from django.contrib.postgres.fields import ArrayField

import random

# Create your models here.
class Pet(models.Model):
    pet_number = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    weight = models.FloatField()
    owner = models.ForeignKey(
        Account, 
        related_name="pets", 
        on_delete=models.CASCADE
        )

    def save(self, *args, **kwargs):
        if not self.pet_number:
            while True:
                random_number = random.randint(00000, 99999)
                self.pet_number = str(random_number)
                try:
                    super(Pet, self,).save(*args, **kwargs)
                except IntegrityError:
                    continue
                break
        else:
            super(Pet, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Treat(models.Model):
    name = models.CharField(max_length=100)
    portion_size = models.CharField(max_length=100)
    caleories_per_portion = models.FloatField()

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=50)
    portion_size = models.FloatField()
    serving_recommendation = models.CharField(max_length=100)
    caleories_per_portion = models.FloatField()

    def __str__(self):
        return self.name

class Diet(models.Model):
    name = models.CharField(max_length=50)
    food = models.ManyToManyField(
        Food,
        related_name='diets',
        unique=False
    )
    treats = models.ManyToManyField(
        Treat,
        related_name='diets'
    )
    def __str__(self):
        return self.name
    
class PetHealth(models.Model):
    pet = models.OneToOneField(
        Pet,
        on_delete=models.CASCADE
    )
    
    weight = models.FloatField()
    temperature_latest = models.FloatField()
    last_checkup_date = models.DateField()
    next_checkup_date = models.DateField()
    diet = models.ForeignKey(
        Diet,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.pet.name
    
class FoodServing(models.Model):
    pet_health = models.ForeignKey(
        PetHealth,
        on_delete=models.CASCADE
    )
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name='food_servings'
    )
    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE
    )
    date_given = models.DateTimeField(auto_now_add=True)
    number_of_portions = models.IntegerField()    

class TreatServing(models.Model):
    pet_health = models.ForeignKey(
        PetHealth,
        on_delete=models.CASCADE
    )
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name='treat_servings'
    )
    treat = models.ForeignKey(
        Treat,
        on_delete=models.CASCADE
    )
    date_given = models.DateTimeField(auto_now_add=True)
    number_of_portions = models.IntegerField()    

class PetDailyDiet(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='daily_diets')
    date = models.DateField()
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE)

#For this code create a django model for a daily diet schedule