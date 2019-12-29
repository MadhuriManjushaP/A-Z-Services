#from django.db import models

# Create your models here.
#from django.db import models

# Create your models here.
from django.db import models
GENDER_CHOICES=[
    ('male','Male'),
    ('female','Female')
]
# creating table for userdetails using django model
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
#     creating a table for disease using django model
class Disease(models.Model):
    
    Disease_name = models.CharField(max_length=255)
    Did=models.IntegerField()
    Symptoms=models.CharField(max_length=600)
    Sid=models.IntegerField()
    class Meta:
        db_table = "Disease"
# creating a table for symptoms using django model
class Symptoms(models.Model):
      Did=models.IntegerField()
      Sid= models.IntegerField()
      Sname=models.CharField(max_length=500)
      class Meta:
          db_table = "Symptoms"
# creating a table for conversations using django model
class Conversations(models.Model):
    Cid=models.IntegerField()
    Sid=models.IntegerField()
    class Meta:
        db_table = "Conversations"
# creating table for conversation questions using django model
class ConversationQuestions(models.Model):
    Cid=models.IntegerField()
    Qid=models.IntegerField()
    class Meta:
        db_table = "ConversationQuestions"
#  creating a table for questions using django model
class Questions(models.Model):
    Qid=models.IntegerField()
    Qnames=models.CharField(max_length=500)
    class Meta:
        db_table = "Questions"                


