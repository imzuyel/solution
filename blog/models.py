from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Blog(models.Model):
	title=models.CharField(max_length=100,default="URI Online Judge | 100")
	name=models.CharField(max_length=100)
	description=models.CharField(max_length=100)
	problem=models.TextField()
	time=models.CharField(max_length=50,default="Timelimit: 1")
	input_p=models.CharField(max_length=7,default="Input")
	input_description=models.TextField()
	output_p=models.CharField(max_length=7,default="Output")
	output_description=models.TextField()
	pub_date=models.TimeField()
	image=models.ImageField(upload_to='images/')
	posted_by=models.ForeignKey(User,on_delete=models.CASCADE)
	solution=models.CharField(max_length=10,default="Solution")
	solution_java=models.TextField()
	solution_c=models.TextField()
	submit=models.CharField(max_length=150,default="https://www.urionlinejudge.com.br/judge/en/runs/add/")

	def summary(self):
		return self.problem[:100]
		
	def pub_date_pretty():
		return self.pub_date.strftime('%b %e, %Y')

	def __str__(self):
		return self.name







   

  
    

 