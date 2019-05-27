from django import forms
from testapp.models import CarModels,SpareParts,CarBrands,Register,LoginModel
from django.conf import settings
from django.contrib.auth.models import User
class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name',]
class LoginForm(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(widget=forms.PasswordInput,max_length=30)
class CarDetailForm(forms.ModelForm):
    class Meta:
        model=CarModels
        fields='__all__'
class SparePartsForm(forms.ModelForm):
    class Meta:
        model=SpareParts
        fields='__all__'
class CarBrandsForm(forms.ModelForm):
    class Meta:
        model=CarBrands
        fields='__all__'
