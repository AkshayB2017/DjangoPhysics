from django.db import models
from django.forms import ModelForm
# Create your models here.
class Question(models.Model):
    n=models.DecimalField(max_digits=5,decimal_places=2)
    t=models.DecimalField(max_digits=5,decimal_places=2)
    v=models.DecimalField(max_digits=5,decimal_places=2)
#P=nRT/V R is constant
class InputForm(ModelForm):
    class Meta:
        model=Question
        fields = "__all__"
    