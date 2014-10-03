from django.conf.urls import patterns, include, url
from django.conf.urls import *
from django.contrib import admin
from account.views import AccountView, AccountPDF, AddWeightView, AddHeightView, AddPositionView, AddScoreView, AddParentView, AddPersonalView, AddCoachView, AddTargetListView
from scout.views import ScoutView
from video.views import VideoView, AddVideoView
from workout.views import WorkoutView

admin.autodiscover()

urlpatterns = patterns('',
        # Examples:
        # url(r'^$', 'myapp.views.home', name='home'),
        # url(r'^myapp/', include('myapp.urls')),

        # Uncomment the admin/doc line below to enable admin documentation:
        # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

        url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS

        url(r'^admin/', include(admin.site.urls)),
        url(r'^login/$', 'django.contrib.auth.views.login'),
        url(r'^logout/$', 'django.contrib.auth.views.logout'),
	url(r'^$', AccountView.as_view(), name='base'),
	url(r'^videos/$', VideoView.as_view(), name='video'),
	url(r'^videos/add/$', AddVideoView.as_view(), name='video_add'),
	url(r'^account/$', AccountView.as_view(), name='account'),
	url(r'^account/pdf/$', AccountPDF.as_view(), name='account_pdf'),
	url(r'^account/add/weight/$', AddWeightView.as_view(), name='account_weight_add'),
	url(r'^account/add/height/$', AddHeightView.as_view(), name='account_height_add'),
	url(r'^account/add/position/$', AddPositionView.as_view(), name='account_position_add'),
	url(r'^account/add/score/$', AddScoreView.as_view(), name='account_score_add'),
	url(r'^account/add/parent/$', AddParentView.as_view(), name='account_parent_add'),
	url(r'^account/add/coach/$', AddCoachView.as_view(), name='account_coach_add'),
	url(r'^account/add/personal/$', AddPersonalView.as_view(), name='account_personal_add'),
	url(r'^account/add/schools/$', AddTargetListView.as_view(), name='account_schools_add'),
	url(r'^scout/$', ScoutView.as_view(), name='scout'),
	url(r'^workout/', WorkoutView.as_view(), name='workout'),
)
