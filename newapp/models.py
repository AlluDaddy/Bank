from django.db import models

# Create your models here.

class Details(models.Model):  
    name = models.CharField(max_length=100,blank=True, null=True)
    password = models.CharField(max_length=100,blank=True, null=True)
    email = models.EmailField(max_length=100,blank=True, null=True)
    mobile=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name