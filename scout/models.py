from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from account.models import Account

class CriterionScaleRow(models.Model):
	rank = models.CharField(max_length=255, blank=False, null=False)
	column_one = models.CharField(max_length=255, blank=False, null=False)
	column_two = models.CharField(max_length=255, blank=True, null=True)
	scale = models.ForeignKey("CriterionScale")
	
	class Meta:
		ordering = ['rank']
		verbose_name_plural = "Grade"
	
class CriterionScale(models.Model):
	name = models.CharField(max_length=255, blank=False, null=False)
	column_one_name = models.CharField(max_length=255, blank=False, null=False)
	column_two_name = models.CharField(max_length=255, blank=True, null=True)
	
	class Meta:
		verbose_name_plural = "Grading Scales"
		
	def __unicode__(self):
		return unicode(self.name)

class Criterion(models.Model):
	name = models.CharField(max_length=255, blank=False, null=False)
	
	def __unicode__(self):
		return unicode(self.name)
		
	class Meta:
		ordering = ['name']
		verbose_name_plural = "criteria"
		
class CriterionRank(models.Model):
	rank = models.PositiveIntegerField()
	created_date = models.DateTimeField(default=timezone.now())
	#criterion = models.ForeignKey(CriterionScale)
	scoutsheet = models.ForeignKey("ScoutSheet")
	scale = models.ForeignKey("CriterionScale")
	#account = models.ForeignKey(Account)
	
	def __unicode__(self):
		return unicode('[' + self.scale.name + '] - ' + str(self.rank) )
	
	class Meta:
		ordering = ['-created_date']
		verbose_name_plural = "Rankings"
	
class ScoutSheet(models.Model):
	account = models.ForeignKey(Account)
	created_date = models.DateTimeField(default=timezone.now())
	scout = models.CharField("Scout", max_length=255, blank=True, null=True)
	note = models.TextField("Physical Description", blank=True, null=True)
	note2 = models.TextField("Abilities", blank=True, null=True)	
	note3 = models.TextField("Weaknesses", blank=True, null=True)	
	note4 = models.TextField("Signability and Player Summation", blank=True, null=True)
	dates_seen = models.TextField("Dates Seen", blank=True, null=True)	
	ab_seen = models.CharField("At Bats Seen", max_length=255, blank=True, null=True)
 	games_seen = models.CharField("Games Seen", max_length=255, blank=True, null=True)
	report_count = models.CharField("Report Count", max_length=255, blank=True, null=True)
	date_completed = models.DateTimeField("Date completed", default=timezone.now())
	makeup = models.CharField("Makeup", max_length=255, blank=True, null=True)
	role = models.CharField("Role:", max_length=255, blank=True, null=True)
	ofp = models.CharField("OFP", max_length=255, blank=True, null=True)
	
	scale = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'))
	player_type_choices = (('Position Player','Position Player'),('Pitcher','Pitcher'),('Both','Both'))
	player_type = models.CharField("Player Type", max_length=10, choices=player_type_choices, blank=True, null=True)
	
	ratings_hitting_ability_p = models.CharField("Hitting Ability - Present", max_length=10, choices=scale, blank=True, null=True)
	ratings_hitting_ability_f = models.CharField("Hitting Ability - Future", max_length=10, choices=scale, blank=True, null=True)
	ratings_raw_power_p = models.CharField("Raw Power - Present", max_length=10, choices=scale, blank=True, null=True)
	ratings_raw_power_f = models.CharField("Raw Power - Future", max_length=10, choices=scale, blank=True, null=True)
	ratings_game_power_p = models.CharField("Game Power - Present", max_length=10, choices=scale, blank=True, null=True)
	ratings_game_power_f = models.CharField("Game Power - Future", max_length=10, choices=scale, blank=True, null=True)
	ratings_running_speed_p = models.CharField("Running Speed - Present", max_length=10, choices=scale, blank=True, null=True)
	ratings_running_speed_f = models.CharField("Running Speed - Future", max_length=10,  choices=scale, blank=True, null=True)
	ratings_base_running_p = models.CharField("Base Running - Present", max_length=10,  choices=scale, blank=True, null=True)
	ratings_base_running_f = models.CharField("Base Running - Future", max_length=10, choices=scale, blank=True, null=True)
	ratings_arm_strength_p = models.CharField("Arm Strength - Present", max_length=10, choices=scale, blank=True, null=True)
	ratings_arm_strength_f = models.CharField("Arm Strength - Future", max_length=10, choices=scale, blank=True, null=True)
	ratings_arm_accuracy_p = models.CharField("Arm Accuracy - Present", max_length=10, choices=scale, blank=True, null=True)
	ratings_arm_accuracy_f = models.CharField("Arm Accuracy - Future", max_length=10, choices=scale, blank=True, null=True)
	ratings_fielding_p = models.CharField("Fielding - Present", max_length=10, choices=scale, blank=True, null=True)
	ratings_fielding_f = models.CharField("Fielding - Future", max_length=10, choices=scale, blank=True, null=True)
	ratings_range_p = models.CharField("Range - Present", max_length=10, choices=scale, blank=True, null=True)
	ratings_range_f = models.CharField("Range - Future", max_length=10, choices=scale, blank=True, null=True)
	
	hit_type = models.CharField("Hit Type", max_length=255, blank=True, null=True)
	hit_approach = models.CharField("Hit Approach", max_length=255, blank=True, null=True)
	time_to_1b = models.CharField("Time to 1B", max_length=255, blank=True, null=True)
	time_to_right = models.CharField("Time to Right", max_length=255, blank=True, null=True)
	
	
	ratings_fb_velocity_p = models.CharField("FB Velocity - Present", max_length=10, choices=scale, blank=True, null=True)
	ratings_fb_velocity_f = models.CharField("FB Velocity - Future", max_length=10, choices=scale, blank=True, null=True)
	ratings_fb_velocity_h = models.CharField("FB Velocity - High", max_length=10, blank=True, null=True)
	ratings_fb_velocity_l = models.CharField("FB Velocity - Low", max_length=10, blank=True, null=True)
	ratings_fb_velocity_pc = models.CharField("FB Velocity - Present Command", max_length=10, choices=scale, blank=True, null=True)
	ratings_fb_velocity_fc = models.CharField("FB Velocity - Future Command", max_length=10, choices=scale, blank=True, null=True)
	ratings_fb_movement_p = models.CharField("FB Movement - Present", max_length=10, choices=scale, blank=True, null=True)
	ratings_fb_movement_f = models.CharField("FB Movement - Future", max_length=10, choices=scale, blank=True, null=True)
	ratings_fb_movement_n = models.CharField("FB Movement - Notes", max_length=255, blank=True, null=True)
	
	ratings_curve_p = models.CharField("Curveball - Present", max_length=10, choices=scale, blank=True, null=True)
	ratings_curve_f = models.CharField("Curveball - Future", max_length=10, choices=scale, blank=True, null=True)
	ratings_curve_h = models.CharField("Curveball - High", max_length=10, blank=True, null=True)
	ratings_curve_l = models.CharField("Curveball - Low", max_length=10, blank=True, null=True)
	ratings_curve_pc = models.CharField("Curveball - Present Command", max_length=10, choices=scale, blank=True, null=True)
	ratings_curve_fc = models.CharField("Curveball - Future Command", max_length=10, choices=scale, blank=True, null=True)
	
	ratings_slider_p = models.CharField("Slider - Present", max_length=10, choices=scale, blank=True, null=True)
	ratings_slider_f = models.CharField("Slider - Future", max_length=10, choices=scale, blank=True, null=True)
	ratings_slider_h = models.CharField("Slider - High", max_length=10, blank=True, null=True)
	ratings_slider_l = models.CharField("Slider - Low", max_length=10, blank=True, null=True)
	ratings_slider_pc = models.CharField("Slider - Present Command", max_length=10, choices=scale, blank=True, null=True)
	ratings_slider_fc = models.CharField("Slider - Future Command", max_length=10, choices=scale, blank=True, null=True)
	
	ratings_change_p = models.CharField("Change - Present", max_length=10, choices=scale, blank=True, null=True)
	ratings_change_f = models.CharField("Change - Future", max_length=10, choices=scale, blank=True, null=True)
	ratings_change_h = models.CharField("Change - High", max_length=10, blank=True, null=True)
	ratings_change_l = models.CharField("Change - Low", max_length=10, blank=True, null=True)
	ratings_change_pc = models.CharField("Change - Present Command", max_length=10, choices=scale, blank=True, null=True)
	ratings_change_fc = models.CharField("Change - Future Command", max_length=10, choices=scale, blank=True, null=True)
	
	ratings_other_p = models.CharField("Other Pitch - Present", max_length=10, choices=scale, blank=True, null=True)
	ratings_other_f = models.CharField("Other Pitch - Future", max_length=10, choices=scale, blank=True, null=True)
	ratings_other_h = models.CharField("Other Pitch - High", max_length=10, blank=True, null=True)
	ratings_other_l = models.CharField("Other Pitch - Low", max_length=10, blank=True, null=True)
	ratings_other_pc = models.CharField("Other Pitch - Present Command", max_length=10, choices=scale, blank=True, null=True)
	ratings_other_fc = models.CharField("Other Pitch - Future Command", max_length=10, choices=scale, blank=True, null=True)
	
	ratings_control_p = models.CharField("Control - Present", max_length=10, choices=scale, blank=True, null=True)
	ratings_control_f = models.CharField("Control - Future", max_length=10, choices=scale, blank=True, null=True)
	ratings_pitchability_p = models.CharField("Pitchability - Present", max_length=10, choices=scale, blank=True, null=True)
	ratings_pitchability_f = models.CharField("Pitchability - Future", max_length=10, choices=scale, blank=True, null=True)
	ratings_delivery_p = models.CharField("Delivery - Present", max_length=10, choices=scale, blank=True, null=True)
	ratings_delivery_f = models.CharField("Delivery - Future", max_length=10, choices=scale, blank=True, null=True)
	ratings_arm_action_p = models.CharField("Arm Action - Present", max_length=10, choices=scale, blank=True, null=True)
	ratings_arm_action_f = models.CharField("Arm Action - Future", max_length=10, choices=scale, blank=True, null=True)

	
	delivery = models.TextField("Delivery", blank=True, null=True)	
	arm_action = models.TextField("Arm Action", blank=True, null=True)	
	arm_slot = models.CharField("Arm Slot", max_length=255, blank=True, null=True)
	
	makeup_athleticism = models.CharField("Athleticism", max_length=10, choices=scale, blank=True, null=True)
	makeup_aptitude = models.CharField("Aptitude", max_length=10, choices=scale, blank=True, null=True)
	makeup_character = models.CharField("Character", max_length=10, choices=scale, blank=True, null=True)
	makeup_dedication = models.CharField("Dedication", max_length=10, choices=scale, blank=True, null=True)
	makeup_instinct = models.CharField("Instinct", max_length=10, choices=scale, blank=True, null=True)
	makeup_aggressiveness = models.CharField("Aggresiveness", max_length=10, choices=scale, blank=True, null=True)
	makeup_confidence = models.CharField("Confidence", max_length=10, choices=scale, blank=True, null=True)
	makeup_maturity = models.CharField("Maturity", max_length=10, choices=scale, blank=True, null=True)
	makeup_competitiveness = models.CharField("Competitiveness", max_length=10, choices=scale, blank=True, null=True)
	
	def ranks(self):
		return CriterionRank.objects.filter(scoutsheet=self.id)
	
	def __unicode__(self):
		return unicode('[' + self.account.user.last_name + '] ' + self.note)
	
	class Meta:
		ordering = ['-created_date']
		verbose_name_plural = "Scout Sheets"
