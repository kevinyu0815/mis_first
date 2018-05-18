from django.db import models

# Create your models here.
class MemberTable(models.Model):
	name = models.CharField(max_length = 200, default='DEFAULT VALUE')
	email = models.CharField(max_length = 200, default='DEFAULT VALUE')
	password = models.CharField(max_length = 200, default='DEFAULT VALUE')
	gender = models.CharField(max_length = 200, default='DEFAULT VALUE')
	birthday = models.CharField(max_length = 200, default='DEFAULT VALUE')

	def __str__(self):
		return (self.email)

