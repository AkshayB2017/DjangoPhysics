from django.db import models
from django.forms import ModelForm
# Create your models here.
class Question(models.Model):
    m=models.DecimalField(max_digits=5,decimal_places=2)
    a=models.DecimalField(max_digits=5,decimal_places=2)
class InputForm(ModelForm):
    class Meta:
        model=Question
        fields = "__all__"
    