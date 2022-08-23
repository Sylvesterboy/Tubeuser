from django.db import models

# Create your models here.
gen=(('male','Male'),('female','Female'))
class Customer(models.Model):
    uid = models.IntegerField()
    name = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    gender = models.CharField(max_length=50,choices=gen,default='Male')
    email = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=200)
    mobile = models.CharField(max_length=50)
    pics = models.ImageField(upload_to="images/",default='default.jpg') 

class MyVideos(models.Model):
    title = models.CharField(max_length=200,default='Not Available')
    category = models.CharField(max_length=200,default='Not Available')
    pdate = models.CharField(max_length=100,default='15/Oct/2019')
    brand = models.CharField(max_length=100,default='Not Available')
    videos = models.FileField(upload_to='videos/', null=True, verbose_name="")
