from django.db import models

# Create your models here.
class Event(models.Model):
    sno = models.AutoField(primary_key=True)
    user = models.CharField(max_length=70)
    name = models.CharField(max_length=200)
    performers = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    image = models.CharField(max_length=2000)
    date = models.DateField()
    time = models.TimeField()
    desc = models.TextField()

    def __str__(self):
        return self.name
    
    
