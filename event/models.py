from django.db import models
from django.db.models.signals import post_save,post_delete,pre_save,m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mail

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.name


class Event(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    date=models.DateField()
    time=models.TimeField()
    location=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="events")

    def __str__(self):
        return self.name
    

class Participant(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    events=models.ManyToManyField(Event,related_name='participants')

    def __str__(self):
        return self.name




   
