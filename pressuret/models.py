from django.db import models
from django.forms import ModelForm
# Create your models here.

TEMP = (
    (0, 'K'),
    (1, 'C'),
    (2, 'F')
)

VOL = (
    (1, 'L'),
    (0.001, 'm³'),
    (1000,'mL')
)

class Question(models.Model):
    n=models.DecimalField(max_digits=5,decimal_places=2)
    t=models.DecimalField(max_digits=5,decimal_places=2)
    tunit=models.FloatField(max_length=10,choices=TEMP)
    v=models.DecimalField(max_digits=5,decimal_places=2)
    vunit=models.FloatField(max_length=10,choices=VOL)
#P=nRT/V R is constant
class InputForm(ModelForm):
    class Meta:
        model=Question
        fields = "__all__"
    