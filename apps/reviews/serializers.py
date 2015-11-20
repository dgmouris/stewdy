from .models import TutorProfile,StudentProfile
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
	bio = serializers.CharField(max_length=500)
	user = UserSerializer(many=False)

	class Meta:
		model = TutorProfile
		fields = ('rating', 'specialization', 'bio','user')
