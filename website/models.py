from django.db import models

# Create your models here.
class Image(models.Model):
	imageID = models.CharField(max_length=30, default="ID")
	imageName = models.TextField(default="Name")
	image = models.ImageField(upload_to='img')


	def __str__(self):
		return f'{self.imageID},{self.imageName},{self.image}'

class Games(models.Model):
	gameID = models.CharField(max_length=30, default="ID")
	gameName = models.TextField(default="Name")
	gameDescription = models.TextField(default="Description")
	gameImage = models.ImageField(upload_to='img')


	def __str__(self):
		return f'{self.gameID},{self.gameName},{self.gameDescription},{self.gameImage}'