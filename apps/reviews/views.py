#core
import json
#django 
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
#third party
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import RetrieveUpdateDestroyAPIView 
from rest_framework.generics import ListCreateAPIView
#app
from .serializers import UserSerializer
from .serializers import StudentProfileSerializer
from .serializers import TutorProfileSerializer
from .serializers import ReviewListSerializer
from .serializers import TutorProfileCreateSerializer
from .serializers import ReviewSerializer
from .serializers import StudentProfileCreateSerializer
from .models import TutorProfile,StudentProfile,TutorReviews


class ReviewMixin(object):
	queryset = TutorReviews.objects.all()
	serializer_class = ReviewSerializer

class StudentProfileList(APIView):
	def get(self, request, format=None):
		student_profiles = StudentProfile.objects.all()
		serializer = StudentProfileSerializer(
			student_profiles,
			many=True)
		return Response(serializer.data)

class TutorProfileList(APIView):
	def get(self,request, format=None):
		tutor_profiles = TutorProfile.objects.all();
		serializer = TutorProfileSerializer(
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
		serializer = StudentProfileSerializer(
			student_profile,
			many=False)
		return Response(serializer.data)

class StudentProfileCreate(APIView):
	def get_user(self,username):
		try:
			user = User.objects.get(username=username)
			return user.id
		except ObjectDoesNotExist:
			raise Http404

	def post(self,request,format=None):
		data = request.data.copy()
		data = data.dict()
		print request.user.username
		user_id = self.get_user(username=request.user.username)
		data['user'] = user_id
		print data
		serializer = StudentProfileCreateSerializer(data=data)
		print "is it valid"
		print serializer.is_valid()
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class TutorProfileDetail(APIView):
	def get_profile(self,slug):
		try:
			return TutorProfile.objects.get(slug=slug)
		except ObjectDoesNotExist:
			raise Http404

	def get(self,request,slug,format=None):
		tutor_profile = self.get_profile(slug=slug)
		serializer = TutorProfileSerializer(
			tutor_profile,
			many=False)
		return Response(serializer.data) 	

class TutorProfileCreate(APIView):
	def get_user(self,username):
		try:
			user = User.objects.get(username=username)
			return user.id
		except ObjectDoesNotExist:
			raise Http404

	def post(self,request,format=None):
		data = request.data.copy()
		data = data.dict()
		print request.user.username
		user_id = self.get_user(username=request.user.username)
		data['user'] = user_id
		print data
		serializer = TutorProfileCreateSerializer(data=data)
		print "is it valid"
		print serializer.is_valid()
		if serializer.is_valid():
			serializer.save()			
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	

class TutorReviewsList(APIView):
	def get_reviews(self,slug):
		try:
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
		serializer = ReviewListSerializer(
			reviews,
			many=True)
		return Response(serializer.data)

class TutorReviewCreate(APIView):
	#permissions_classes = (IsAuthenticated,)

	def get_tutor(self,slug):
		try:
			return TutorProfile.objects.get(slug=slug)
		except ObjectDoesNotExist:
			raise Http404
	def get_student(self,user):
		try:
			return StudentProfile.objects.get(user=user)
		except ObjectDoesNotExist:
			raise Http404
		
	
	def post(self,request,slug,format=None):
		data = request.data.copy()
		data = data.dict()
		tutor = self.get_tutor(slug=slug)
		student = self.get_student(user=request.user)
		data['tutor'] = tutor.pk 
		data['student'] = student.pk

		serializer = ReviewSerializer(data=data)
		if serializer.is_valid():
			serializer.save()			
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


