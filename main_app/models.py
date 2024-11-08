from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import DO_NOTHING


# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=15)
    salery=models.CharField(max_length=6)
    date=models.DateField()


class Login(AbstractUser):
    is_donor=models.BooleanField(default=False)
    is_receiver=models.BooleanField(default=False)

class Doner(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name="Doner")
    name=models.CharField(max_length=20)
    age=models.CharField(max_length=3)
    DOB=models.DateField()
    BloodGroup = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+','B-'),
        ('O+','O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),

    )
    Blood = models.CharField(max_length=3, choices=BloodGroup)
    Address=models.TextField()
    Phone=models.CharField(max_length=10)
    Email = models.EmailField()
    document = models.FileField(upload_to='documents/')

class Receiver(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE,related_name="Receiver")
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=3)
    DOB = models.DateField()
    BloodGroup = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-','B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    )
    Blood = models.CharField(max_length=3, choices=BloodGroup)
    Address = models.TextField()
    Phone = models.CharField(max_length=10)
    Email=models.EmailField()
    document = models.FileField(upload_to='documents/')

class Receiver_request(models.Model):
    ReceiverName=models.ForeignKey('Receiver',on_delete=models.CASCADE)
    DonerName=models.ForeignKey('Doner',on_delete=DO_NOTHING,blank=True,null=True)
    date=models.DateField()
    BloodGroup = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    )
    Blood = models.CharField(max_length=3, choices=BloodGroup)
    HospitalName=models.CharField(max_length=30)
    Place=models.CharField(max_length=30)
    Contact=models.CharField(max_length=10)
    Status=models.IntegerField(default=0)

class feedback(models.Model):
    name=models.ForeignKey("Receiver",on_delete=models.CASCADE)
    massage=models.TextField()
    date=models.DateField(auto_now=True)
    replay=models.CharField(max_length=200,null=True,blank=True)


