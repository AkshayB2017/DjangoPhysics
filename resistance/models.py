from django.db import models
from django.forms import ModelForm
# Create your models here.
class Question(models.Model):
    l=models.DecimalField(max_digits=5,decimal_places=2)
    a=models.DecimalField(max_digits=5,decimal_places=2)
#R= rho*l/a rho constant
class InputForm(ModelForm):
    class Meta:
        model=Question
        fields = "__all__"
    