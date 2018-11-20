from django.db import models
from django.forms import ModelForm
# Create your models here.
TIME=(
    (float(0.001),'ms'),
    (float(1),'s'),
    (float(60),'min'),
    (float(3600),'hr')
)
CHARGE=(
    (float(1),'C'),
    (float(1000),'KC')
)

class Question(models.Model):
    q=models.DecimalField(max_digits=5,decimal_places=2)
    Qunit=models.FloatField(max_length=10, choices=CHARGE)
    t=models.DecimalField(max_digits=5,decimal_places=2)
    Tunit=models.FloatField(max_length=10, choices=TIME)
#i=Q/t
class InputForm(ModelForm):
    class Meta:
        model=Question
        fields = "__all__"