from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

    
class contact_form(models.Model):
    fname = models.CharField(max_length=30, null=True)
    lname=models.CharField(null=True,max_length=100)
    email = models.EmailField(max_length=30,null=True)
    phone = models.IntegerField(null=True)
    Message =models.CharField(null=True,max_length=10000000000000)
    
    
