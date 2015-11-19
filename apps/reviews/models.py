from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class TutorProfile(models.Model):
	user = models.OneToOneField(User)
	rating = models.FloatField(null=True,  blank=True)
	specialization = models.TextField(null=True,blank=True)
	bio = models.TextField(null=True,blank=True)
	
	def __unicode__(self):
		return self.user.username

class StudentProfile(models.Model):
	user = models.OneToOneField(User)
	education = models.CharField(max_length=200,null=True, blank=True)

	def __unicode__(self):
		return self.user.username

class TutorReviews(models.Model):
	rating = models.FloatField(null=True, blank=True)
	review = models.TextField(null=True,blank=True)
	tutor = models.ForeignKey(TutorProfile)
	student = models.ForeignKey(StudentProfile)
	created = models.DateTimeField(auto_now_add=True, default=datetime.today())
	updated = models.DateTimeField(auto_now=True, default=datetime.today())

	def __unicode__(self):
		return self.review
