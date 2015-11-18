from django.db import models
from django.conf import settings
from datetime import datetime
# Create your models here.

class TutorProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	rating = models.FloatField(null=True,  blank=True)
	specialization = models.TextField(null=True,blank=True)
	bio = models.TextField(null=True,blank=True)
	
	def __str__(self):
		return self.user.username

class TutorReviews(models.Model):
	rating = models.FloatField(null=True, blank=True)
	review = models.TextField(null=True,blank=True)
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	created = models.DateTimeField(auto_now_add=True, default=datetime.today())
	updated = models.DateTimeField(auto_now=True, default=datetime.today())

	#def __unicode__(self):
	#	return self.review
