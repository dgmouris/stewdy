from django.conf.urls import patterns, include, url
import views
# from .views import StudentProfileList

urlpatterns = patterns('',

    url(r'^/student/$', views.StudentProfileList.as_view(),name='tutors'),
 	url(r'^/tutor/$', views.TutorProfileList.as_view(), name='students'),
    url(r'^/student/(?P<slug>[\w-]+)/$', views.StudentProfileDetail.as_view(), name='student'),
    url(r'^/tutor/(?P<slug>[\w-]+)/$', views.TutorProfileDetail.as_view(), name='tutor'),
    url(r'^/tutor/(?P<slug>[\w-]+)/reviews$', views.TutorReviewsList.as_view(), name='reviews'),
    url(r'^/tutor/(?P<slug>[\w-]+)/review$',views.TutorReviewCreate.as_view(),name='review'),
)


