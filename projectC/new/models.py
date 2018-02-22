from django.db import models

# Create your models here.
class Challenge(models.Model):
	name = models.CharField(max_length=125)
	content= models.TextField()
	image = models.ImageField(null=True)
	created_on =models.DateTimeField(auto_now_add=True)
	updated_on =models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name