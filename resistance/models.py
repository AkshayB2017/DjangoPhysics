from django.db import models
from django.forms import ModelForm
# Create your models here.
LENGTH=(
    (float(1),'m'),
    (float(.01),'cm'),
    (float(0.001),'mm')
)
AREA=(
    (float(0.0001),'cm²'),
    (float(1),'m²')
)
class Question(models.Model):
    l=models.DecimalField(max_digits=5,decimal_places=2)
    Lunit=models.FloatField(max_length=10,choices=LENGTH)
    a=models.DecimalField(max_digits=5,decimal_places=2)
    Aunit=models.FloatField(max_length=10,choices=AREA)
#R= rho*l/a rho constant
class InputForm(ModelForm):
    class Meta:
        model=Question
        fields = "__all__"
    