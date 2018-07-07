from django.db import models

# Create your models here.
class Clubinfo(models.Model):
	
	club_text = models.CharField(max_length=2000)
	club_name= models.CharField(max_length=100)
	def __str__(self):
		return self.club_text


    

