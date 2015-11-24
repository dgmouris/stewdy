from django.conf.urls import patterns, include, url
import views
# from .views import StudentProfileList

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stewdy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/v1/student/$', views.StudentProfileList.as_view(),name='tutors'),
 	url(r'^api/v1/tutor/$', views.TutorProfileList.as_view(), name='students'),
    url(r'^api/v1/student/(?P<slug>[\w-]+)/$', views.StudentProfileDetail.as_view(), name='student'),
    url(r'^api/v1/tutor/(?P<slug>[\w-]+)/$', views.TutorProfileDetail.as_view(), name='tutor'),
    url(r'^api/v1/tutor/(?P<slug>[\w-]+)/reviews$', views.TutorReviewsList.as_view(), name='reviews'),
    url(r'^api/v1/tutor/(?P<slug>[\w-]+)/review$',views.TutorReviewCreate.as_view(),name='review'),
)











