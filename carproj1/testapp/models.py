from django.db import models
class Register(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    dob=models.DateField()
    email=models.EmailField()
    passord1=models.CharField(max_length=30)
    passord2=models.CharField(max_length=30)

class LoginModel(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
class CarBrands(models.Model):
    brand=models.CharField(max_length=60)
    country=models.CharField(max_length=60)
    def __str__(self):
        return self.brand
class CarModels(models.Model):
    TYPE_CHOICES=(('HatchBack','HatchBack'),('Seden','Seden'),('SUV','SUV'),('MUV','MUV'))
    FUEL_CHOICES=(('PETROL','PETROL'),('DIESEL','DIESEL'))
    brand=models.ForeignKey(CarBrands,related_name='cbrand')
    model=models.CharField(max_length=60)
    year=models.IntegerField()
    type=models.CharField(max_length=30,choices=TYPE_CHOICES)
    fuel=models.CharField(max_length=30,choices=FUEL_CHOICES)
    price=models.FloatField()
    def __str__(self):
        return self.model
class SpareParts(models.Model):
    model=models.ForeignKey(CarModels,related_name='cmodel')
    spoiler=models.IntegerField(blank=True,null=True)
    wheels=models.IntegerField(blank=True,null=True)
    brakes=models.IntegerField(blank=True,null=True)
    headlamps=models.IntegerField(blank=True,null=True)
    taillamps=models.IntegerField(blank=True,null=True)
    airbags=models.IntegerField(blank=True,null=True)
    clutchplates=models.IntegerField(blank=True,null=True)


# Create your models here.
