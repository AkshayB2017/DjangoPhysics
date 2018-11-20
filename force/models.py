from django.db import models
from django.forms import ModelForm
# Create your models here.
ACCEL=(
    (float(1),'m/s2'),
    (0.27777777777778,'km/hr2')
)

MASS=(
    (float(1),'kg'),
    (float(100),'tonne'),
    (float(.001),'g')
)
class Question(models.Model):
    m=models.DecimalField(max_digits=5,decimal_places=2)
    Munit=models.FloatField(max_length=7, choices=MASS)
    a=models.DecimalField(max_digits=5,decimal_places=2)
    Aunit=models.FloatField(max_length=7, choices=ACCEL)
class InputForm(ModelForm):
    class Meta:
        model=Question
        fields = "__all__"
    