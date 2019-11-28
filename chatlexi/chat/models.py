#from django.db import models

# Create your models here.
#from django.db import models

# Create your models here.
from django.db import models
GENDER_CHOICES=[
    ('male','Male'),
    ('female','Female')
]
class UserDetails(models.Model):
    
    name = models.CharField(max_length=255)
    age=models.IntegerField()
    gender=models.CharField(choices=GENDER_CHOICES,max_length=6)
    height=models.IntegerField()
    weight=models.IntegerField()
    smoke=models.BooleanField()
    drink=models.BooleanField()
    diabetes=models.BooleanField()
    highbp=models.BooleanField()
    
    
    

def __str__(self):

    return self.name
