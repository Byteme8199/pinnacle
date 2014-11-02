from functools import update_wrapper
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.admin.templatetags.admin_urls import add_preserved_filters
from django.core.exceptions import PermissionDenied
from django.shortcuts import render


from workout.models import WorkoutWeek, Exercise, Workout
# from workout.forms import ManageWorkoutForm
from django.db import models



class WeirdWorkoutAdmin(ModelAdmin):
	change_form_template = 'admin/workout/change_form.html'
	manage_view_template = 'admin/workout/manage_view.html'

	def get_urls(self):
		from django.conf.urls import patterns, url
 
		def wrap(view):
			def wrapper(*args, **kwargs):
				return self.admin_site.admin_view(view)(*args, **kwargs)
			return update_wrapper(wrapper, view)

		info = self.model._meta.app_label, self.model._meta.model_name

		urls = patterns('',
			url(r'^(.+)/manage/$',
			wrap(self.manage_view),
			name='%s_%s_manage' % info),
		)

		super_urls = super(WorkoutAdmin, self).get_urls()

		return urls + super_urls


	def manage_view(self, request, id, form_url='', extra_context=None):
		opts = Workout._meta
		form = ManageWorkoutForm()
		obj = Workout.objects.get(pk=id)
		
		if not self.has_change_permission(request, obj):
			raise PermissionDenied

		# Management stuff here

			

		#######################

		preserved_filters = self.get_preserved_filters(request)
		form_url = add_preserved_filters({'preserved_filters': preserved_filters, 'opts': opts}, form_url)

		context = {
			'title': 'Manage %s' % obj,
			'has_change_permission': self.has_change_permission(request, obj),
			'form_url': form_url,
			'opts': opts,
			'errors': form.errors,
			'app_label': opts.app_label,
			'original': obj,
		}
		
		context.update(extra_context or {})

		return render(request, self.manage_view_template, context)









class WeekAdmin(admin.ModelAdmin):
	model = WorkoutWeek

class ExerciseInline(admin.TabularInline):
	model = Exercise

class WorkoutAdmin(admin.ModelAdmin):
	model = Workout
	inlines = [ExerciseInline]

admin.site.register(Workout, WorkoutAdmin)
#admin.site.register(ExerciseName)

