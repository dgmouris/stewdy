from django.contrib import admin
from .models import TutorProfile, TutorReviews, StudentProfile
# Register your models here.
class TutorProfileAdmin(admin.ModelAdmin):
	class Meta:
		model = TutorProfile

class TutorReviewsAdmin(admin.ModelAdmin):
	class Meta:
		model = TutorReviews

class StudentProfileAdmin(admin.ModelAdmin):
	class Meta:
		model = StudentProfile

admin.site.register(TutorProfile,TutorProfileAdmin)
admin.site.register(TutorReviews,TutorReviewsAdmin)
admin.site.register(StudentProfile,StudentProfileAdmin)
