from django.db import models
from django.forms import ModelForm

AREA = (
    (1, 'm²'),
    (0.0001, 'cm²')
)

THICKNESS = (
    (1, 'm'),
    (0.01, 'cm'),
    (1000, 'km')
)

TEMP = (
    (0, 'K'),
    (1, 'C'),
    (2, 'F')
)

# Create your models here.

class Question(models.Model):
    a=models.DecimalField(max_digits=5,decimal_places=2)
    aunit=models.FloatField(max_length=10,choices=AREA)
    t=models.DecimalField(max_digits=5,decimal_places=2)
    tunit=models.FloatField(max_length=10,choices=TEMP)
    d=models.DecimalField(max_digits=5,decimal_places=2)
    dunit=models.FloatField(max_length=10,choices=THICKNESS)


#https://www.khanacademy.org/science/physics/thermodynamics/specific-heat-and-heat-transfer/a/what-is-thermal-conductivity
# P=k*a*t/l   t is temperature difference, a is area, l is length
class InputForm(ModelForm):
    class Meta:
        model=Question
        fields = "__all__"
    