from django.db import models
from django.forms import ModelForm
# Create your models here.
FORCE=((float(1),'N'),
        (float(1000),'kN')
    )
AREA=(  (float(1),'m2'),
        (float(10000),'cm2'),
        (float(1000000),'cm2')
    )
class Question(models.Model):
    f=models.DecimalField(max_digits=10,decimal_places=2)
    Funit=models.FloatField(max_length=10, choices=FORCE)
    a=models.DecimalField(max_digits=10,decimal_places=2)
    Aunit=models.FloatField(max_length=10, choices=AREA)
class InputForm(ModelForm):
    class Meta:
        model=Question
        fields = "__all__"
    