from django.db import models
from django.forms import ModelForm
# Create your models here.
class Question(models.Model):
    a=models.DecimalField(max_digits=5,decimal_places=2)
    t=models.DecimalField(max_digits=5,decimal_places=2)
    d=models.DecimalField(max_digits=5,decimal_places=2)
#https://www.khanacademy.org/science/physics/thermodynamics/specific-heat-and-heat-transfer/a/what-is-thermal-conductivity
# P=k*a*t/l   t is temperature difference, a is area, l is length
class InputForm(ModelForm):
    class Meta:
        model=Question
        fields = "__all__"
    