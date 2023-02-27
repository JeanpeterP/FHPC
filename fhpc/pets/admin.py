from django.contrib import admin
from .models import Pet, PetHealth
# Register your models here.

class PetHealthInline(admin.TabularInline):
    model = PetHealth

class PetAdmin(admin.ModelAdmin):
    model = Pet
    list_display = (
        'pet_number',
        'name',
        'breed',
        'age',
        'weight',
        'owner',
    )
    inlines = [PetHealthInline]
    
admin.site.register(Pet, PetAdmin)
