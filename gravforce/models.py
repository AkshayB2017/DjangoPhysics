from django.db import models
from django.forms import ModelForm
# Create your models here.
class Question(models.Model):
    m1=models.DecimalField(max_digits=5,decimal_places=2)
    m2=models.DecimalField(max_digits=5,decimal_places=2)
    r=models.DecimalField(max_digits=5,decimal_places=2)
#Fg=-Gm1m2/(r^2)
class InputForm(ModelForm):
    class Meta:
        model=Question
        fields = "__all__"
    