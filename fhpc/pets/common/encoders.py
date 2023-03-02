from .json import ModelEncoder
from appointments.models import Appointments
from rest_framework import serializers
from accounts.models import Account
from pets.models import Pet, PetHealth

class AppointmentEncoder(ModelEncoder):
    model = Appointments
    properties = ["customer", "pet", "start_time", "end_time","location","notes"]

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["pk", "username", "email", "first_name", "last_name"]


class PetSerializer(serializers.ModelSerializer):
    owner = AccountSerializer(many=False)
    
    class Meta:
        model = Pet
        fields = ["name", "breed", "age", "weight", "owner"]

class AppointmentSerializer(serializers.ModelSerializer):
    customer = AccountSerializer(many=False)
    pet = PetSerializer(many=False)

    class Meta:
        model = Appointments
        fields = ["customer", "pet", "start_time", "end_time", "location", "notes"]
    
class PetHealthSerializer(serializers.ModelSerializer):
    diet = serializers.StringRelatedField()

    class Meta:
        model = PetHealth
        fields = ["weight", "temperature_latest", "last_checkup_date", "next_checkup_date", "diet"]

class PetSerializer(serializers.ModelSerializer):
    owner = AccountSerializer(many=False)
    pethealth = PetHealthSerializer(many=False)

    class Meta:
        model = Pet
        fields = ["name", "breed", "age", "weight", "owner", "pethealth"]