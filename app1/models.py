from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class work(models.Model):
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_pic = models.ImageField(upload_to='profile_pic/',null=True)
    Name_worker = models.CharField(max_length=20,null=True)
    adhar_no = models.CharField(max_length=16,null=True)
    age = models.CharField(max_length=3,null=True)
    city = models.CharField(max_length=10,null=True)
    Type_of_work = models.ForeignKey(work,on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=15,null=True)
    available = (('select_status', '--Select status--'), ('YES', 'YES'), ('NO', 'NO'))
    status = models.CharField(max_length=50, help_text="status", choices=available, default="",null=True)
    contact = models.CharField(max_length=10,null=True)
    role = (('select_status', '--Select status--'), ('HINDI', 'HINDI'), ('ENGLISH', 'ENGLISH'), ('PUNJABI', 'PUNJABI'), ('Other', 'Other'))
    language = models.CharField(max_length=50, help_text="status", choices=role, default="",null=True)
    charge_per_day = models.CharField(max_length=10,null=True)
    rating = models.CharField(max_length=10,null=True,default="")
    resume = models.FileField(upload_to='resumes/',null=True)
    post = models.CharField(max_length=50,null=True,default="")
    insta = models.CharField(max_length=50,null=True,default="")
    fb = models.CharField(max_length=50,null=True,default="")
    twt = models.CharField(max_length=50,null=True,default="")


    def __str__(self):
        return f'{self.Name_worker}'


class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    O_name = models.CharField(max_length=10,null=True)
    address = models.CharField(max_length=15,null=True)
    adhar_no = models.CharField(max_length=16,null=True)

    def __str__(self):
        return f'{self.user}'



class Owner_work(models.Model):

    person_name = models.CharField(max_length=100)
    work_dec = models.CharField(max_length=50)
    work_type = models.CharField(max_length=100)
    pay_for_work = models.CharField(max_length=10)
    place = models.CharField(max_length=10,default="")
    time = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.work_type}'


class Booked(models.Model):

    b_woker = models.CharField(max_length=50,null=True,default=None)
    b_woker_id = models.CharField(max_length=50,null=True,default=None)
    b_work = models.CharField(max_length=50,null=True,default=None)
    b_Owner = models.CharField(max_length=50,null=True,default=None)
    role = (('select_status', '--Select status--'), ('Accept', 'Accept'), ('Reject', 'Reject'))
    action = models.CharField(max_length=50, help_text="status", choices=role, default="", null=True)

    def __str__(self):
        return f'{self.id}'


class Room(models.Model):
    name = models.CharField(max_length=1000)

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)