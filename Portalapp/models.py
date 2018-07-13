from django.db import models

# Create your models here.
class Clubinfo(models.Model):
	
	club_text = models.CharField(max_length=2000)
	club_name= models.CharField(max_length=100)
	image=models.CharField(max_length=200,blank=True)
	def __str__(self):
		return self.club_text
		
class form(models.Model):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=100)  
    date = models.CharField(max_length=100)
    info = models.CharField(blank=True,max_length=1000)
    email= models.EmailField()
    phone= models.CharField(max_length=100)
    address= models.CharField(max_length=1000)
    club=models.CharField(max_length=100,null=True)
    approval=models.IntegerField(default=0)
class admin(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    club_name = models.CharField(max_length=100)
	
class form2(models.Model):
    approval=models.CharField(max_length=10)


    

