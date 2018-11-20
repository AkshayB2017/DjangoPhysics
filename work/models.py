from django.db import models
from django.forms import ModelForm
# Create your models here.

DISP=(
        (float(1),'m'),
        (float(1000),'km'),
        (float(0.01),'cm')
    )
FORCE=(
        (float(1),'N'),
        (float(1000),'kN')
    )

class Question(models.Model):
    f=models.DecimalField(max_digits=5,decimal_places=2)
    Funit=models.FloatField(max_length=10, choices=FORCE)
    d=models.DecimalField(max_digits=5,decimal_places=2)
    Dunit=models.FloatField(max_length=10, choices=DISP)
    
class InputForm(ModelForm):
    class Meta:
        model=Question
        fields = "__all__"
    