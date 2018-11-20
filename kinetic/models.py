from django.db import models
from django.forms import ModelForm

MASS = (
    (1, 'g'),
    (1000, 'kg'),
)

VELOCITY = (
    (1, 'm/s'),
    (0.27777, 'km/h')
)

# Create your models here.

class Question(models.Model):
    m=models.DecimalField(max_digits=5,decimal_places=2)
    munit=models.FloatField(max_length=10,choices=MASS)
    v=models.DecimalField(max_digits=5,decimal_places=2)
    vunit=models.FloatField(max_length=10,choices=VELOCITY)
#e=0.5mv^2
class InputForm(ModelForm):
    class Meta:
        model=Question
        fields = "__all__"
    