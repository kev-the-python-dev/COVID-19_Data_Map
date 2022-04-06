import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text

class CovidData(models.Model):
    Province_State=models.CharField(max_length=100)
    Last_Update=models.CharField(max_length=100)
    Lat=models.CharField(max_length=100)
    Long=models.CharField(max_length=100)
    Confirmed=models.CharField(max_length=100)
    Deaths=models.CharField(max_length=100)
    Case_Fatality_Ration=models.CharField(max_length=100)
