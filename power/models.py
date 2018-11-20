from django.db import models
from django.forms import ModelForm
# Create your models here.
FORCE=((float(1),'N'),
        (float(1000),'kN')
    )
TIME=(
    (float(1),'s'),
    (float(60),'min'),
    (float(3600),'hr')
)
class Question(models.Model):
    f=models.DecimalField(max_digits=10,decimal_places=2)
    Funit=models.FloatField(max_length=10, choices=FORCE)
    T=models.DecimalField(max_digits=10,decimal_places=2)
    Tunit=models.FloatField(max_length=10, choices=TIME)
class InputForm(ModelForm):
    class Meta:
        model=Question
        fields = "__all__"
    