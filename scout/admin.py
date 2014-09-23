from django.contrib import admin
from scout.models import *
	
class CriterionRankInline(admin.TabularInline):
	model = CriterionRank
	fields = ('criterion', 'rank', 'created_date', 'account')
	readonly_fields = ['created_date',]
	extra = 5

class CriterionAdmin(admin.ModelAdmin):
	list = ""
	
class ScoutSheetAdmin(admin.ModelAdmin):
	list_filter = ('account', 'note', 'created_date')
	list_display = ('account', 'note', 'created_date')
	search_fields = ['note','created_date','account']
	raw_id_fields = ('account',)
	inlines = [CriterionRankInline]

admin.site.register(Criterion, CriterionAdmin)
admin.site.register(ScoutSheet, ScoutSheetAdmin)