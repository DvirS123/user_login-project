from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
	'''
	the project will take
	-title-charfield
	-date-datefield
	-body-textfield
	-uploaded-datefield
	-image-imagefield
	'''
	Title = models.CharField(max_length = 100)
	Source = models.URLField(max_length = 100)
	Date = models.DateTimeField()
	Body = models.TextField()
	Votes = models.PositiveIntegerField(default = 1)
	Uploaded = models.DateField(auto_now = False, auto_now_add =True)
	Image = models.ImageField(upload_to ='product_images/')
	Icon = models.ImageField(upload_to= 'product_icons/')
	User_name = models.ForeignKey(User, on_delete=models.CASCADE)


	def modified_date(self):
		return self.Date.strftime('%b / %e / %Y')
	def summarry(self):
		return self.Body[:100]