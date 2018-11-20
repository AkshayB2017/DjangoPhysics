from django.db import models
from django.forms import ModelForm
# Create your models here.
class Question(models.Model):
    q=models.DecimalField(max_digits=5,decimal_places=2)
    t=models.DecimalField(max_digits=5,decimal_places=2)
#i=Q/t
class InputForm(ModelForm):
    class Meta:
        model=Question
        fields = "__all__"