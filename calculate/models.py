from django.db import models
from django.forms import ModelForm
# Create your models here.

SPEED=(
    (float(1),'m/s'),
    (float(5/18),'km/hr')
)
TIME=(
    (float(1),'s'),
    (float(60),'min'),
    (float(3600),'hr')
)
ACCEL=(
    (float(1),'m/s2'),
    (0.27777777777778,'km/hr2')
)

class Question(models.Model):
    u=models.DecimalField(max_digits=5,decimal_places=2)
    Uunit=models.FloatField(max_length=3, choices=SPEED)
    t=models.DecimalField(max_digits=5,decimal_places=2)
    Tunit=models.FloatField(max_length=3, choices=TIME)
    a=models.DecimalField(max_digits=5,decimal_places=2)
    Aunit=models.FloatField(max_length=3, choices=ACCEL)
    #unit=
class InputForm(ModelForm):
    class Meta:
        model=Question
        fields = ['u','Uunit','t','Tunit','a','Aunit']
    