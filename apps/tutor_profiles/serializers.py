from .models import TutorProfile, TutorReviews

from rest_framework import serializers

class TutorProfileSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = TutorProfile
		fields = ('user.username','rating','specialization','bio')


