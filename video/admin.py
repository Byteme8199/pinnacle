from django.contrib import admin
from video.models import Video, VideoType, VideoReply
from django.db import models

class VideoReplyInline(admin.TabularInline):
	model = VideoReply
	fields = ('file', 'video_embed', 'note')
	readonly_fields = ['created_date']
	extra = 1
	
class VideoTypeAdmin(admin.ModelAdmin):
	list_filter = ('created_date',)
	list_display = ('name', 'created_date')
	
class VideoAdmin(admin.ModelAdmin):
	list_filter = ('created_date', 'account', 'video_type')
	list_display = ('title', 'thumbnail', 'video_type', 'created_date')
	#date_hierarchy = 'created_date'
	search_fields = ['title','video_type','created_date','account']
	raw_id_fields = ('account',)
	inlines = [VideoReplyInline]

admin.site.register(VideoType, VideoTypeAdmin)	
admin.site.register(Video, VideoAdmin)