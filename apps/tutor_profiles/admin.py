from django.contrib import admin
from .models import TutorProfile, TutorReviews 
# Register your models here.
class TutorProfileAdmin(admin.ModelAdmin):
	class Meta:
		model = TutorProfile

class TutorReviewsAdmin(admin.ModelAdmin):
	class Meta:
		model = TutorReviews


admin.site.register(TutorProfile,TutorProfileAdmin)
admin.site.register(TutorReviews,TutorReviewsAdmin)
