from django.db import models

# Create your models here.

class Author(models.Model):
	name = models.CharField(max_length=100)
	gender=models.CharField(max_length=1)
	date = models.DateField()
	
	def __str__(self):
		return "%s" % (self.name)

class Book(models.Model):
	title = models.CharField(max_length=100)
	pub_date = models.DateField()
	genre=models.CharField(max_length=30)
	isbn=models.CharField(max_length=13)
	author = models.ManyToManyField(Author)
	
	def __str__(self):
		return self.title
