from django.conf.urls import patterns, include, url
import views
# from .views import StudentProfileList

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stewdy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/v1/student/$', views.StudentProfileList.as_view()),
)











