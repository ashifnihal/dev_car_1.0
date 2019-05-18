from testapp.models import CarBrands,CarModels
from django import forms
class CarBrandForm(forms.ModelForm):
    class Meta:
        model=CarBrands
        fields='__all__'
        
