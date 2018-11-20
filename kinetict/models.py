from django.db import models
from django.forms import ModelForm

TEMP = (
    (0, 'K'),
    (1, 'C'),
    (2, 'F')
)

# Create your models here.
class Question(models.Model):
    n=models.DecimalField(max_digits=5,decimal_places=2)
    t=models.DecimalField(max_digits=5,decimal_places=2)
    tunit=models.FloatField(max_length=10,choices=TEMP)
#delta U= 3/2 * n*R*t (R constant)
class InputForm(ModelForm):
    class Meta:
        model=Question
        fields = "__all__"
    