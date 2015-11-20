from django.shortcuts import render
from .models import TutorProfile,StudentProfile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .serializers import ListStudentProfileSerializer
from .serializers import ListTutorProfileSerializer


class StudentProfileList(APIView):
	def get(self, request, format=None):
		student_profiles = StudentProfile.objects.all()
		serializer = ListStudentProfileSerializer(
			student_profiles,
			many=True)
		return Response(serializer.data)

class TutorProfileList(APIView):
	def get(self,request, format=None):
		tutor_profiles = TutorProfile.objects.all();
		serializer = ListTutorProfileSerializer(
			tutor_profiles,
			many=True)
		return Response(serializer.data) 