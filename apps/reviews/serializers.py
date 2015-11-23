from .models import TutorProfile,StudentProfile, TutorReviews
from django.contrib.auth.models import User
from rest_framework import serializers


#default user serializers
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields=('username','first_name','last_name','email')
 

class ListStudentProfileSerializer(serializers.Serializer):
	#add the user as a hyperlinked field
	education = serializers.CharField(max_length=200) 
	user = UserSerializer(many=False)

	class Meta:
		model = StudentProfile
		fields = ('education','user')

class ListTutorProfileSerializer(serializers.Serializer):
	rating =  serializers.FloatField(max_value=5.0, min_value=0.0)
	specialization = serializers.CharField(max_length=500) 
	education = serializers.CharField(max_length=200) 
	bio = serializers.CharField(max_length=500)
	user = UserSerializer(many=False)

	class Meta:
		model = TutorProfile
		fields = ('rating', 'specialization', 'bio','user')

class TutorProfileDetailSerializer(serializers.Serializer):
	rating =  serializers.FloatField(max_value=5.0, min_value=0.0)
	specialization = serializers.CharField(max_length=500) 
	education = serializers.CharField(max_length=200) 
	bio = serializers.CharField(max_length=500)
	user = UserSerializer(many=False)

	class Meta:
		model = TutorProfile
		fields = ('rating', 'specialization', 'bio','user')

class StudentProfileDetailSerializer(serializers.Serializer):
	#add the user as a hyperlinked field
	education = serializers.CharField(max_length=200) 
	user = UserSerializer(many=False)

	class Meta:
		model = StudentProfile
		fields = ('education','user')

class ReviewSerializer(serializers.Serializer):
	
	rating = serializers.FloatField(max_value=5.0, min_value=0.0)
	review = serializers.CharField(max_length=600)
	#tutor = TutorProfileDetailSerializer(many=False)
	#student = StudentProfileDetailSerializer(many=False)
	created = serializers.DateTimeField()
	updated = serializers.DateTimeField()

	class Meta:
		model = TutorReviews
		fields = ('tutor','student','rating','review','created','updated')
