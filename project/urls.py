from django.conf.urls import patterns, include, url
from django.conf.urls import *
from django.contrib import admin
from account.views import AccountView, AccountPDF, AddWeightView, AddHeightView, AddPositionView, AddScoreView, AddParentView, AddPersonalView, EditPersonalView, AddCoachView, AddTargetListView, AddPhotoView, AddSchoolView, AddTeamPhotoView, GhostView
from scout.views import ScoutView
from video.views import VideoView, AddVideoView, PhotoView
from workoutsheet.views import WorkoutView, WorkoutWeekView, WorkoutBaseView, WorkoutVideosView, WorkoutWorkoutsView, WorkoutWarmupView, WorkoutCoreView, WorkoutPlyometricView, WorkoutVideosByIDView, WorkoutPDF

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myapp.views.home', name='home'),
    # url(r'^myapp/', include('myapp.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS

    # url(r'^admin/workout/$', WorkoutView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
	url(r'^$', AccountView.as_view(), name='base'),		
	url(r'^videos/$', VideoView.as_view(), name='video'),
	url(r'^videos/add/$', AddVideoView.as_view(), name='video_add'),
	url(r'^photo/$', PhotoView.as_view(), name='video_photo_reply_view'),				   
	url(r'^account/$', AccountView.as_view(), name='account'),
	url(r'^account/pdf/$', AccountPDF.as_view(), name='account_pdf'),
	url(r'^account/add/photo/(?P<pk>\d+)/$', AddPhotoView.as_view(), name='account_photo_add'),
	url(r'^account/add/team_photo/(?P<pk>\d+)/$', AddTeamPhotoView.as_view(), name='account_team_photo_add'),
	url(r'^account/add/school/(?P<pk>\d+)/$', AddSchoolView.as_view(), name='account_school_add'),
	url(r'^account/add/weight/$', AddWeightView.as_view(), name='account_weight_add'),
	url(r'^account/add/height/$', AddHeightView.as_view(), name='account_height_add'),
	url(r'^account/add/position/$', AddPositionView.as_view(), name='account_position_add'),
	url(r'^account/add/score/$', AddScoreView.as_view(), name='account_score_add'),
	url(r'^account/add/parent/$', AddParentView.as_view(), name='account_parent_add'),
	url(r'^account/add/coach/$', AddCoachView.as_view(), name='account_coach_add'),
	url(r'^account/edit/personal/(?P<pk>\d+)/$', EditPersonalView.as_view(), name='account_personal_edit'),
	url(r'^account/edit/ghost/(?P<pk>\d+)/$', GhostView.as_view(), name='account_ghost_edit'),
	url(r'^account/add/personal/$', AddPersonalView.as_view(), name='account_personal_add'),
	url(r'^account/add/schools/$', AddTargetListView.as_view(), name='account_schools_add'),
	url(r'^scout/$', ScoutView.as_view(), name='scout'),
	url(r'^workout/$', WorkoutBaseView.as_view(), name='workout'),
	url(r'^workout/pdf/(?P<workout_id>\d+)/$', WorkoutPDF.as_view(), name='workout_pdf'),
	url(r'^workout/videos/$', WorkoutVideosView.as_view(), name='workout_videos'),
	url(r'^workout/videos/(?P<pk>\d+)/$', WorkoutVideosByIDView.as_view(), name='workout_videos_by_id'),
	url(r'^workout/workouts/$', WorkoutWorkoutsView.as_view(), name='workout_workouts'),
	url(r'^workout/warmup/$', WorkoutWarmupView.as_view(), name='workout_warmup'),
	url(r'^workout/core/$', WorkoutCoreView.as_view(), name='workout_core'),
	url(r'^workout/plyometric/$', WorkoutPlyometricView.as_view(), name='workout_plyo'),
	url(r'^workout/workouts/(?P<pk>\d+)/$', WorkoutView.as_view(), name='workout_view'),
	url(r'^workout/week/(?P<pk>\d+)/$', WorkoutWeekView.as_view(), name='workout_week_view'),
#	url(r'^workout/create/$', CreateWorkout.as_view(), name='create_workout'),
#	url(r'^workout/exercise/create/(?P<workout_id>\d+)/$', AddExercisesToWorkout.as_view(), name='exercises_plus_workout'),
#	url(r'^workout/set/create/(?P<workout_id>\d+)/$', AddExerciseSetsToExercise.as_view(), name='exercise_set_plus_workout'),
#	url(r'^workout/edit/routine/(?P<pk>\d+)/$', EditRoutineView.as_view(), name='workout_routine_edit'),
#	url(r'^workout/edit/day/(?P<pk>\d+)/$', EditDayView.as_view(), name='workout_day_edit'),
	#url(r'^workout/edit/exerciseset/$', EditExerciseSetView.as_view(), name='workout_exerciseset_edit'),
					   
)
