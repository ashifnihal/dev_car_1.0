from django import forms
from testapp.models import CarModels,SpareParts
class CarDetailForm(forms.ModelForm):
    class Meta:
        model=CarModels
        fields='__all__'
class SparePartsForm(forms.ModelForm):
    class Meta:
        model=SpareParts
        fields='__all__'
