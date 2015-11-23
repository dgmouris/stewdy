from django.shortcuts import render
from .models import TutorProfile,StudentProfile,TutorReviews
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializers import UserSerializer
from .serializers import ListStudentProfileSerializer
from .serializers import ListTutorProfileSerializer
from .serializers import ReviewSerializer
from django.core.exceptions import ObjectDoesNotExist

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

class StudentProfileDetail(APIView):
	
	def get_profile(self,slug):
		try:
			return StudentProfile.objects.get(slug=slug)
		except ObjectDoesNotExist:
			raise Http404

	def get(self,request, slug,format=None):
		student_profile = self.get_profile(slug=slug)
		serializer = ListStudentProfileSerializer(
			student_profile,
			many=False)
		return Response(serializer.data)

class TutorProfileDetail(APIView):
	def get_profile(self,slug):
		try:
			return TutorProfile.objects.get(slug=slug)
		except ObjectDoesNotExist:
			raise Http404

	def get(self,request,slug,format=None):
		tutor_profile = self.get_profile(slug=slug)
		serializer = ListTutorProfileSerializer(
			tutor_profile,
			many=False)
		return Response(serializer.data) 	


class TutorReviewsList(APIView):
	def get_reviews(self,slug):
		try:
			tutor = TutorProfile.objects.all().get(slug=slug)
			return TutorReviews.objects.all().filter(tutor=tutor)

		except ObjectDoesNotExist:
			raise Http404

	def get_student(self,slug):
		try:
			return StudentProfile.objects.get(slug=slug)
		except ObjectDoesNotExist:
			raise Http404


	def get_tutor(self,slug):
		try:
			return TutorProfile.objects.get(slug=slug)
		except ObjectDoesNotExist:
			raise Http404
			
	def get(self,request,slug,format=None):
		reviews = self.get_reviews(slug=slug)
		serializer = ReviewSerializer(
			reviews,
			many=True)
		return Response(serializer.data)
