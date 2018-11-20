from django.db import models
from django.forms import ModelForm
# Create your models here.

MASS=(
    (float(1),'kg'),
    (float(100),'tonne'),
    (float(.001),'g')
)

DISP=(
    (float(1),'m'),
    (float(1000),'km'),
    (float(0.01),'cm')
)

class Question(models.Model):
    m=models.DecimalField(max_digits=7,decimal_places=2)
    Munit=models.FloatField(max_length=7, choices=MASS)
    r=models.DecimalField(max_digits=7,decimal_places=2)
    Runit=models.FloatField(max_length=7, choices=DISP)
#g=-Gm/r^2
class InputForm(ModelForm):
    class Meta:
        model=Question
        fields = "__all__"
    