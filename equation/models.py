from django.db import models
from django.forms import ModelForm
# Create your models here.
ACCEL=(
    (float(1),'m/s2'),
    (0.27777777777778,'km/hr2')
)
SPEED=(
    (float(1),'m/s'),
    (float(5/18),'km/hr')
)
DISP=(
    (float(1),'m'),
    (float(1000),'km'),
    (0.01,'cm')
)

class Question(models.Model):    
    u=models.DecimalField(max_digits=5,decimal_places=2)
    Uunit=models.FloatField(max_length=3, choices=SPEED)
    a=models.DecimalField(max_digits=5,decimal_places=2)
    Aunit=models.FloatField(max_length=3, choices=ACCEL)
    s=models.DecimalField(max_digits=5,decimal_places=2)
    Sunit=models.FloatField(choices=DISP)
class InputForm(ModelForm):
    class Meta:
        model=Question
        fields = "__all__"