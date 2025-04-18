from django.db import models

# Create your models here.
class owner(models.Model):
    o_id=models.AutoField(primary_key=True)
    email=models.EmailField()
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=15)

class coach(models.Model):
    c_id=models.AutoField(primary_key=True)
    coachname=models.CharField(max_length=200,default='ydghuyg')
    birthdate=models.DateField()
    gender=models.CharField(max_length=10)
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=100)
    mobilenumber=models.CharField(max_length=11)
    experience=models.CharField(max_length=15)
    joindate=models.DateField()
    enddate=models.DateField()
    photo=models.ImageField(upload_to='coach/', default='000')
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

class player1(models.Model):
    p_id=models.AutoField(primary_key=True)
    playername=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    email=models.EmailField(max_length=50)
    mobileno=models.CharField(max_length=20)
    birthdate=models.DateField()
    gender=models.CharField(max_length=10)
    height=models.CharField(max_length=15)
    weight=models.CharField(max_length=15)
    position=models.CharField(max_length=20)
    joindate=models.DateField()
    enddate=models.DateField()
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=15)
    photo=models.ImageField(upload_to='player/')

class Team(models.Model):
    t_id=models.AutoField(primary_key=True)
    teamname=models.CharField(max_length=50)
    schedule=models.CharField(max_length=200)
    coach_name=models.ForeignKey(coach,on_delete=models.SET_NULL,null=True)

class assign_tb(models.Model):
    a_id=models.AutoField(primary_key=True)
    coa_id=models.ForeignKey(coach,on_delete=models.SET_NULL,null=True)
    tea_id=models.ForeignKey(Team,on_delete=models.SET_NULL,null=True)
    ply_id=models.ForeignKey(player1,on_delete=models.SET_NULL,null=True)

class schedule1(models.Model):
    coa_id=models.ForeignKey(coach,on_delete=models.SET_NULL,null=True)
    tm_id=models.ForeignKey(Team,on_delete=models.SET_NULL,null=True)
    description=models.CharField(max_length=30)
    Address=models.CharField(max_length=100)
    startdate=models.DateField()
    enddate=models.DateField()
    starttime=models.CharField(max_length=20)
    endtime=models.CharField(max_length=20)
    role=models.CharField(max_length=30)
    man_of_match=models.CharField(max_length=50)

