from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.fields import SlugField
from django.db.models.signals import post_save
# Create your models here.

class TutorProfile(models.Model):
	user = models.OneToOneField(User)
	education = models.CharField(max_length=200,null=True, blank=True)
	rating = models.FloatField(null=True,  blank=True)
	specialization = models.TextField(null=True,blank=True)
	bio = models.TextField(null=True,blank=True)
	slug = SlugField(max_length=40, null=True, blank=True)
	#,editable=False
	'''
	def save(self):
		super(TutorProfile, self).save()
		self.slug = slugify(self.user.username)
		super(TutorProfile, self).save()
	'''
	def __unicode__(self):
		return self.user.username

class StudentProfile(models.Model):
	user = models.OneToOneField(User)
	education = models.CharField(max_length=200,null=True, blank=True)
	slug = SlugField(max_length=40,null=True, blank=True)
	#,editable=False
	'''
	def save(self):
		#super(StudentProfile, self).save()
		self.slug = slugify(self.user.username)
		super(StudentProfile, self).save()
	'''
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

#signal to create the slug
def create_slug(sender, instance, **kwargs):
     instance.slug = slugify(instance.user.username)
     instance.save()

post_save.connect(create_slug, sender=StudentProfile, dispatch_uid="update_slug")
post_save.connect(create_slug, sender=TutorProfile, dispatch_uid="update_slug")