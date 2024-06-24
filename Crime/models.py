from pydoc import describe
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserType(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

class PoliceStation(models.Model):
    station_name = models.CharField(max_length=50)

class UserReg(models.Model):
    login = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    contact = models.CharField(max_length=50,null=True)
    dob = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

class PoliceReg(models.Model):
    login = models.ForeignKey(User, on_delete=models.CASCADE)
    station = models.ForeignKey(PoliceStation, on_delete=models.CASCADE)
    contact = models.CharField(max_length=50)
    p_location = models.CharField(max_length=50)

class Criminals(models.Model):
    police = models.ForeignKey(PoliceReg, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    age = models.CharField(max_length=50)

class Feedback(models.Model):
    user = models.ForeignKey(UserReg, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=50)


class Complaint(models.Model):

    timee = models.CharField(max_length=50)
    c_date = models.CharField(max_length=50)
    complaint = models.CharField(max_length=100)
    location= models.CharField(max_length=100,null=True)

    user = models.ForeignKey(UserReg, on_delete=models.CASCADE)
    police = models.ForeignKey(PoliceReg, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    status1=models.CharField(max_length=50,null=True)



class Officer_Reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    designation = models.ImageField(upload_to='images/')
    station = models.ForeignKey(PoliceReg, on_delete=models.CASCADE,null=True)


class Fir(models.Model):
    reporttime= models.CharField(max_length=50)
    complaint_id = models.ForeignKey(Complaint,on_delete=models.CASCADE,null=True)
    informer=models.CharField(max_length=500)
    casedescription=models.CharField(max_length=500)
    place=models.CharField(max_length=100)
    criminal=models.CharField(max_length=500)
    explanation=models.CharField(max_length=500)
    datetime = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=200, null=True)


class evidence(models.Model):


    police_id=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    ledger_id=models.ForeignKey(Complaint, on_delete=models.CASCADE,null=True)
    date =models.CharField(max_length=100,null=True)

    filename =models.CharField(max_length=100,null=True)
    filenumber =models.CharField(max_length=100,null=True)
    location =models.CharField(max_length=100,null=True)
 

    location1 =models.CharField(max_length=100,null=True)
    time1 =models.CharField(max_length=100,null=True)
    date1 =models.CharField(max_length=100,null=True)
    evidence1 =models.CharField(max_length=500,null=True)

    location2 =models.CharField(max_length=100,null=True)
    time2 =models.CharField(max_length=100,null=True)
    date2 =models.CharField(max_length=100,null=True)
    evidence2 =models.CharField(max_length=500,null=True)


    location3 =models.CharField(max_length=100,null=True)
    time3 =models.CharField(max_length=100,null=True)
    date3 =models.CharField(max_length=100,null=True)
    evidence3 =models.CharField(max_length=500,null=True)


    location4 =models.CharField(max_length=100,null=True)
    time4=models.CharField(max_length=100,null=True)
    date4 =models.CharField(max_length=100,null=True)
    evidence4 =models.CharField(max_length=500,null=True)


    location5 =models.CharField(max_length=100,null=True)
    time5 =models.CharField(max_length=100,null=True)
    date5 =models.CharField(max_length=100,null=True)
    evidence5 =models.CharField(max_length=500,null=True)


    location6 =models.CharField(max_length=100,null=True)
    time6 =models.CharField(max_length=100,null=True)
    date6 =models.CharField(max_length=100,null=True)
    evidence6 =models.CharField(max_length=500,null=True)


class add_evidence(models.Model):
    user = models.ForeignKey(UserReg, on_delete=models.CASCADE,null=True)
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE,null=True)
    station = models.ForeignKey(PoliceReg, on_delete=models.CASCADE,null=True)
    image=models.ImageField('media/',null=True)
    video=models.ImageField('media/',null=True)
    desc=models.CharField(max_length=100,null=True)


class missing(models.Model):
    user = models.ForeignKey(UserReg, on_delete=models.CASCADE,null=True)
    station = models.ForeignKey(PoliceReg, on_delete=models.CASCADE,null=True)
    station_name = models.CharField(max_length=50,null=True)
    image=models.ImageField('media/',null=True)
    date=models.CharField(max_length=100,null=True)
    desc=models.CharField(max_length=100,null=True)

