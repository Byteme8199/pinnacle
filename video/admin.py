from django.contrib import admin
from video.models import Video, VideoType, VideoReply, PhotoReply
from django.db import models
from django import forms

class VideoReplyInline(admin.StackedInline):
	model = VideoReply
	fields = ('file', 'note')
	readonly_fields = ['created_date']
	extra = 1

class PhotoReplyInline(admin.StackedInline):
	model = PhotoReply
	fields = ('file', 'note')
	readonly_fields = ['created_date']
	extra = 1

class VideoTypeAdmin(admin.ModelAdmin):
	list_filter = ('created_date',)
	list_display = ('name', 'created_date')

class VideoAdmin(admin.ModelAdmin):
	model = Video
	list_filter = ('created_date', 'account', 'video_type')
	list_display = ('title', 'thumbnail', 'video_type', 'created_date')
	#date_hierarchy = 'created_date'
	search_fields = ['title','video_type','created_date','account']
	raw_id_fields = ('account',)
	inlines = [VideoReplyInline, PhotoReplyInline]

	#class Media:
	#	js = ('admin/js/vidsubmit.js',)


admin.site.register(VideoType, VideoTypeAdmin)
admin.site.register(Video, VideoAdmin)
