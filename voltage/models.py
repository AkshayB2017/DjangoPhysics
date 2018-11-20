from django.db import models
from django.forms import ModelForm
# Create your models here.
RESIST=(
    (float(.001),'mΩ'),
    (float(1),'Ω'),
    (float(1000),'kΩ'),
    (float(1000000),'MΩ')
)
CURREN=(
    (float(0.001),'mA'),
    (float(1),'A'),
    (float(1000),'KA')
)
class Question(models.Model):
    i=models.DecimalField(max_digits=5,decimal_places=2)
    Iunit=models.FloatField(max_length=10,choices=CURREN)
    r=models.DecimalField(max_digits=5,decimal_places=2)
    Runit=models.FloatField(max_length=10,choices=RESIST)
#v=ir
class InputForm(ModelForm):
    class Meta:
        model=Question
        fields = "__all__"
    