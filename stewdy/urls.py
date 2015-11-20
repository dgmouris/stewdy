from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # basically the home page
	url(r'^$',include('home.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    # allauth, which is the authentication framework
    url(r'^accounts/', include('allauth.urls')),
    # api for all of the allauth
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
   	#this includes the review api as well as pages.
    url(r'^reviews/',include('reviews.urls')),
)

