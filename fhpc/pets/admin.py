from django import forms
from django.contrib import admin
from .models import Pet, PetHealth, BehavioralQuirks, Medications, Food, FoodAllergy, Treat, FoodServing, TreatServing
# Register your models here.
from django.utils import timezone

class FoodServingForm(forms.ModelForm):
    class Meta:
        model = FoodServing
        fields = '__all__'

    food = forms.ModelChoiceField(
        queryset=Food.objects.all(),
        required=True,
        label='Food'
    )
    number_of_portions = forms.IntegerField(
        required=True,
        label='Number of Portions'
    )

class TreatServingForm(forms.ModelForm):
    class Meta:
        model = TreatServing
        fields = '__all__'

    treat = forms.ModelChoiceField(
        queryset=Treat.objects.all(),
        required=True,
        label='Treat'
    )
    number_of_portions = forms.IntegerField(
        required=True,
        label='Number of Portions'
    )

class AllergiesForm(forms.ModelForm):
    class Meta:
        model = FoodAllergy
        fields = '__all__'

class BehavioralQuirksForm(forms.ModelForm):
    class Meta:
        model = BehavioralQuirks
        fields = '__all__'

class MedicationsForm(forms.ModelForm):
    class Meta:
        model = FoodAllergy
        fields = '__all__'

class PetHealthForm(forms.ModelForm):
    class Meta:
        model = PetHealth
        fields = '__all__'

    # diet = forms.ModelChoiceField(
    #     queryset=Diet.objects.all(),
    #     required=True,
    #     label='Diet'
    # )
    # date = forms.DateField(
    #     required=True,
    #     label='Date',
    #     help_text='Enter date in YYYY-MM-DD format'
    # )

class FoodServingInline(admin.TabularInline):
    model = FoodServing
    extra = 0
    can_delete = True
    min_num = 1
    max_num = 20
    form = FoodServingForm
                           


class TreatServingInline(admin.TabularInline):
    model = TreatServing
    extra = 0
    can_delete = True
    min_num = 1
    max_num = 20
    form = TreatServingForm

    
class PetHealthInline(admin.TabularInline):
    model = PetHealth
    extra = 0
    form = PetHealthForm
    inlines = [FoodServingInline, TreatServingInline]

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
    inlines = [PetHealthInline, FoodServingInline, TreatServingInline]
    
admin.site.register(Pet, PetAdmin)
admin.site.register(BehavioralQuirks)
admin.site.register(Medications)
admin.site.register(FoodAllergy)
admin.site.register(Food)
admin.site.register(Treat)