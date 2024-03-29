from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django import forms
from .models import Account
from pets.models import Pet

User = get_user_model()
# Register your models here.

class PetInline(admin.TabularInline):
    model = Pet

class AccountAdmin(UserAdmin):
    model = Account
    list_display = (
        'account_number',
        'username',
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'zipcode',
        'display_pets'
    )
    filter_horizontal = ('groups', 'user_permissions')
    inlines = [PetInline]
    
    def display_pets(self, obj):
        return ", ".join([pet.name for pet in obj.pets.all()])
    display_pets.short_description = 'Pets'

admin.site.register(Account, AccountAdmin)

