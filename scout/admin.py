from django.contrib import admin
from scout.models import *

class CriterionScaleRowInline(admin.TabularInline):
	model = CriterionScaleRow
	extra = 8

class CriterionScaleAdmin(admin.ModelAdmin):
	inlines = [CriterionScaleRowInline]

class CriterionRankInline(admin.StackedInline):
	model = CriterionRank
	#fields = ('criterion', 'rank', 'created_date', 'account')
	readonly_fields = ['created_date',]
	extra = 5

class CriterionAdmin(admin.ModelAdmin):
	list = ""

class ScoutSheetAdmin(admin.ModelAdmin):
	list_filter = ('account', 'note', 'created_date')
	list_display = ('account', 'note', 'created_date')
	search_fields = ['note','created_date','account']
	raw_id_fields = ('account',)

	fieldsets = (
        ('Personal', {
            'fields': ('account', 'created_date', 'scout', 'player_type', ('show_catcher', 'show_hitting'), ('show_infield', 'show_outfield'))
        }),
		('Scouting', {
            'fields': ('date_completed', ('role', 'ofp'), ('makeup', 'report_count'), ('games_seen', 'ab_seen'), 'dates_seen')
        }),
		('Notes', {
            'fields': ('note', 'note2', 'note3', 'note4')
        }),
        ('Makeup', {
			'classes': ('grp-collapse grp-closed',),
            'fields': ('makeup_athleticism', 'makeup_aptitude', 'makeup_character', 'makeup_dedication', 'makeup_instinct', 'makeup_aggressiveness', 'makeup_confidence', 'makeup_maturity', 'makeup_competitiveness')
        }),
		('Ratings - Hitters', {
			'classes': ('grp-collapse grp-closed',),
            'fields': ('hit_type', 'hit_approach', 'time_to_1b', 'time_to_right', 'ratings_hitting_ability_p', 'ratings_hitting_ability_f', 'ratings_raw_power_p', 'ratings_raw_power_f', 'ratings_game_power_p', 'ratings_game_power_f', 'ratings_running_speed_p', 'ratings_running_speed_f', 'ratings_base_running_p', 'ratings_base_running_f', 'ratings_arm_strength_p', 'ratings_arm_strength_f', 'ratings_arm_accuracy_p', 'ratings_arm_accuracy_f', 'ratings_fielding_p', 'ratings_fielding_f', 'ratings_range_p', 'ratings_range_f')
        }),
		('Ratings - Pitchers', {
			'classes': ('grp-collapse grp-closed',),
            'fields': ('delivery', 'arm_action', 'arm_slot', 'ratings_fb_velocity_p', 'ratings_fb_velocity_f', 'ratings_fb_velocity_h', 'ratings_fb_velocity_l', 'ratings_fb_velocity_pc', 'ratings_fb_velocity_fc', 'ratings_fb_movement_p', 'ratings_fb_movement_f', 'ratings_fb_movement_n', 'ratings_curve_p', 'ratings_curve_f', 'ratings_curve_h', 'ratings_curve_l', 'ratings_curve_pc', 'ratings_curve_fc', 'ratings_slider_p', 'ratings_slider_f', 'ratings_slider_h', 'ratings_slider_l', 'ratings_slider_pc', 'ratings_slider_fc', 'ratings_change_p', 'ratings_change_f', 'ratings_change_h', 'ratings_change_l', 'ratings_change_pc', 'ratings_change_fc', 'ratings_other_p', 'ratings_other_f', 'ratings_other_h', 'ratings_other_l', 'ratings_other_pc', 'ratings_other_fc', 'ratings_control_p', 'ratings_control_f', 'ratings_pitchability_p', 'ratings_pitchability_f', 'ratings_delivery_p', 'ratings_delivery_f', 'ratings_arm_action_p', 'ratings_arm_action_f')
        }),
		('Catcher - Pros', {
			'classes': ('grp-collapse grp-closed',),
            'fields': ('catcher_1', 'catcher_2', 'catcher_3', 'catcher_4', 'catcher_5', 'catcher_6', 'catcher_7', 'catcher_8', 'catcher_9', 'catcher_10', 'catcher_11', 'catcher_12', 'catcher_13', 'catcher_14', 'catcher_15')
        }),
		('Catcher - Cons', {
			'classes': ('grp-collapse grp-closed',),
            'fields': ('catcher_16', 'catcher_17', 'catcher_18', 'catcher_19', 'catcher_20', 'catcher_21', 'catcher_22', 'catcher_23', 'catcher_24', 'catcher_25', 'catcher_26', 'catcher_27', 'catcher_28', 'catcher_29', 'catcher_30')
        }),
		('Hitting - Pros', {
			'classes': ('grp-collapse grp-closed',),
			'fields': ('hitting_1', 'hitting_2', 'hitting_3', 'hitting_4', 'hitting_5', 'hitting_6', 'hitting_7', 'hitting_8', 'hitting_9', 'hitting_10', 'hitting_11', 'hitting_12', 'hitting_13', 'hitting_14')
				}),
		('Hitting - Cons', {
			'classes': ('grp-collapse grp-closed',),
			'fields': ('hitting_16', 'hitting_17', 'hitting_18', 'hitting_19', 'hitting_20', 'hitting_21', 'hitting_22', 'hitting_23', 'hitting_24', 'hitting_25', 'hitting_26', 'hitting_27', 'hitting_28', 'hitting_29')
		}),
		('Infield - Pros', {
			'classes': ('grp-collapse grp-closed',),
			'fields': ('infield_1', 'infield_2', 'infield_3', 'infield_4', 'infield_5', 'infield_6', 'infield_7', 'infield_8', 'infield_9', 'infield_10', 'infield_11', 'infield_12')
				}),
		('Infield - Cons', {
			'classes': ('grp-collapse grp-closed',),
			'fields': ('infield_16', 'infield_17', 'infield_18', 'infield_19', 'infield_20', 'infield_21', 'infield_22', 'infield_23', 'infield_24', 'infield_25', 'infield_26', 'infield_27')
		}),
		('Outfield - Pros', {
			'classes': ('grp-collapse grp-closed',),
			'fields': ('outfield_1', 'outfield_2', 'outfield_3', 'outfield_4', 'outfield_5', 'outfield_6', 'outfield_7', 'outfield_8', 'outfield_9', 'outfield_10', 'outfield_11')
				}),
		('Outfield - Cons', {
			'classes': ('grp-collapse grp-closed',),
			'fields': ('outfield_16', 'outfield_17', 'outfield_18', 'outfield_19', 'outfield_20', 'outfield_21', 'outfield_22', 'outfield_23', 'outfield_24', 'outfield_25', 'outfield_26')
		}),
    )
	
	#inlines = [CriterionRankInline]

admin.site.register(CriterionScale, CriterionScaleAdmin)
admin.site.register(Criterion, CriterionAdmin)
admin.site.register(ScoutSheet, ScoutSheetAdmin)
