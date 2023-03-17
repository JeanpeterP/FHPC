from .json import ModelEncoder
from accounts.models import Account
from pets.models import Pet
from rest_framework import serializers

class AccountDetailEncoder(ModelEncoder):
    model = Account
    properties = ["username", "email", "first_name", "last_name", "is_staff", "zipcode"]

class AccountEncoder(ModelEncoder):
    model = Account
    properties = ["username", "email", "first_name", "last_name"]

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["pk", "username", "email", "first_name", "last_name"]

class AccountSerializerWPassword(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["pk", "username", "email", "password", "first_name", "last_name", "zipcode", "phone_number"]

class PetSerializer(serializers.ModelSerializer):
    owner = AccountSerializer(many=False)
    
    class Meta:
        model = Pet
        fields = ["name", "breed", "age", "weight", "owner"]
