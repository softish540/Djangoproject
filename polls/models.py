from django.db import models
from django.db.models import CASCADE
from django.db.models.deletion import CASCADE


#first create classbase tables.. models are inbuilt packages from django  
#class question(models.model):# models.model transcribes pythonlic database codes to a da structure

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    
class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=CASCADE)
    choice_text=models.CharField(max_length=200)
    votes = models.IntegerField(default=0) 