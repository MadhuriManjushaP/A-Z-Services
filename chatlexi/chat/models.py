#from django.db import models

# Create your models here.
#from django.db import models

# Create your models here.
from django.db import models
GENDER_CHOICES=[
    ('male','Male'),
    ('female','Female')
]
#crete user details  in model Userdetails class and  migrate in  database
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
#create user conversation in model  post class and migrate in database
class Post (models.Model):
    title = models.CharField(max_length=50)
      
    
    

def __str__(self):

    return self.name
