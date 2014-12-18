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
	player_type_choices = (('Position','Position'),('Pitcher','Pitcher'),('Both','Both'))
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
	
	
	show_catcher = models.BooleanField("Show Catcher Pros/Cons", default=0)
	show_hitting = models.BooleanField("Show Hitting Pros/Cons", default=0)
	show_infield = models.BooleanField("Show Infield Pros/Cons", default=0)
	show_outfield = models.BooleanField("Show Outfield Pros/Cons", default=0)

	catcher_1 = models.BooleanField("Shows a primary and secondary position", default=0)
	catcher_2 = models.BooleanField("Footwork in primary is simple/balanced", default=0)
	catcher_3 = models.BooleanField("Footwork in secondary is simple/balanced", default=0)
	catcher_4 = models.BooleanField("Hands are soft and strong", default=0)
	catcher_5 = models.BooleanField("Stops the ball in the strikezone", default=0)
	catcher_6 = models.BooleanField("Stays balanced during the catch", default=0)
	catcher_7 = models.BooleanField("Gets into a good blocking position", default=0)
	catcher_8 = models.BooleanField("Reacts to ball in dirt easily", default=0)
	catcher_9 = models.BooleanField("Gets to his feet easily after block", default=0)
	catcher_10 = models.BooleanField("Clean transition to throwing hand", default=0)
	catcher_11 = models.BooleanField("Simple throwing action", default=0)
	catcher_12 = models.BooleanField("Gains ground to throw", default=0)
	catcher_13 = models.BooleanField("Ball keeps flight through the base", default=0)
	catcher_14 = models.BooleanField("Body size is durable", default=0)
	catcher_15 = models.BooleanField("Made somebody say 'wow'", default=0)
	
	catcher_16 = models.BooleanField("No difference in primary and secondary", default=0)
	catcher_17 = models.BooleanField("Footwork does not provide balance", default=0)
	catcher_18 = models.BooleanField("Hands are heavy at the catch", default=0)
	catcher_19 = models.BooleanField("Does not have strong hands", default=0)
	catcher_20 = models.BooleanField("Takes strikes out of strike zone", default=0)
	catcher_21 = models.BooleanField("Off balance when receiving", default=0)
	catcher_22 = models.BooleanField("Late reaction to block position", default=0)
	catcher_23 = models.BooleanField("Does not get into efficient block position", default=0)
	catcher_24 = models.BooleanField("Struggles to get up after block", default=0)
	catcher_25 = models.BooleanField("Trouble getting ball out of glove", default=0)
	catcher_26 = models.BooleanField("Arm action breaks rhythm", default=0)
	catcher_27 = models.BooleanField("Loses ground to throwing position", default=0)
	catcher_28 = models.BooleanField("Ball loses flight before the base", default=0)
	catcher_29 = models.BooleanField("Body size does not project as durable", default=0)
	catcher_30 = models.BooleanField("Was not noticeable", default=0)
	
	hitting_1 = models.BooleanField("Starts relaxed", default=0)
	hitting_2 = models.BooleanField("Repeats his load", default=0)
	hitting_3 = models.BooleanField("Gets into hitting position on time", default=0)
	hitting_4 = models.BooleanField("Hands don't seperate too early", default=0)
	hitting_5 = models.BooleanField("Keeps rhythm from load to swing", default=0)
	hitting_6 = models.BooleanField("Has time to track the ball", default=0)
	hitting_7 = models.BooleanField("Swing has short path to the ball", default=0)
	hitting_8 = models.BooleanField("Weight transfers under control", default=0)
	hitting_9 = models.BooleanField("Hits against a firm front side", default=0)
	hitting_10 = models.BooleanField("Barrel stays in the zone naturally", default=0)
	hitting_11 = models.BooleanField("Ability to hit for average at next level", default=0)
	hitting_12 = models.BooleanField("Ability to hit for power at the next level", default=0)
	hitting_13 = models.BooleanField("Drives gaps", default=0)
	hitting_14 = models.BooleanField("Made somebody say 'wow'", default=0)

	hitting_16 = models.BooleanField("Tense in stance", default=0)
	hitting_17 = models.BooleanField("Does not repeat his load", default=0)
	hitting_18 = models.BooleanField("Late getting into hitting position", default=0)
	hitting_19 = models.BooleanField("Too early into hitting position", default=0)
	hitting_20 = models.BooleanField("Hands seperate too early and get lost", default=0)
	hitting_21 = models.BooleanField("Loses rhythm from load to swing", default=0)
	hitting_22 = models.BooleanField("Doesn't have time to track ball", default=0)
	hitting_23 = models.BooleanField("Weight sticks on backside", default=0)
	hitting_24 = models.BooleanField("Swing path is long to the ball", default=0)
	hitting_25 = models.BooleanField("Front side is weak", default=0)
	hitting_26 = models.BooleanField("Barrel is in and out of zone quickly", default=0)
	hitting_27 = models.BooleanField("Does not have potential for power", default=0)
	hitting_28 = models.BooleanField("Does not drive through the ball naturally", default=0)
	hitting_29 = models.BooleanField("Was not noticeable", default=0)

	infield_1 = models.BooleanField("Efficient first step in correct direction", default=0)
	infield_2 = models.BooleanField("Feet are under control at catch", default=0)
	infield_3 = models.BooleanField("Hands are under control at catch", default=0)
	infield_4 = models.BooleanField("Glove is relaxed and under the ball", default=0)
	infield_5 = models.BooleanField("Catch is made out in front of body", default=0)
	infield_6 = models.BooleanField("Has flow through the ball", default=0)
	infield_7 = models.BooleanField("Clean transition to throwing hand", default=0)
	infield_8 = models.BooleanField("Easy Arm Action", default=0)
	infield_9 = models.BooleanField("Strong Arm", default=0)
	infield_10 = models.BooleanField("Accurate Arm", default=0)
	infield_11 = models.BooleanField("Has the ability to Catch, Step and Throw", default=0)
	infield_12 = models.BooleanField("Made somebody say 'Wow!'", default=0)

	infield_16 = models.BooleanField("Slow first step losing ground", default=0)
	infield_17 = models.BooleanField("Feet are out of control at catch", default=0)
	infield_18 = models.BooleanField("Hands are heavy at the catch", default=0)
	infield_19 = models.BooleanField("Hands start above and jab to ball", default=0)
	infield_20 = models.BooleanField("Catch is made under body", default=0)
	infield_21 = models.BooleanField("Does not move through the ball", default=0)
	infield_22 = models.BooleanField("Dificult transition to throw hand", default=0)
	infield_23 = models.BooleanField("Long arm action", default=0)
	infield_24 = models.BooleanField("Weak arm", default=0)
	infield_25 = models.BooleanField("Inaccurate arm", default=0)
	infield_26 = models.BooleanField("Can't catch and throw in 1 step", default=0)
	infield_27 = models.BooleanField("Was not noticeable", default=0)


	outfield_1 = models.BooleanField("Efficient reads off the bat", default=0)
	outfield_2 = models.BooleanField("Takes proper angles to the ball", default=0)
	outfield_3 = models.BooleanField("Feet are under control at the catch", default=0)
	outfield_4 = models.BooleanField("Positions body well for catch", default=0)
	outfield_5 = models.BooleanField("Proper footwork after the catch", default=0)
	outfield_6 = models.BooleanField("Clean transfer to throwing hand", default=0)
	outfield_7 = models.BooleanField("Clean arm action, creates backspin", default=0)
	outfield_8 = models.BooleanField("Has a rhythm from catch to throw", default=0)
	outfield_9 = models.BooleanField("Strong arm", default=0)
	outfield_10 = models.BooleanField("Accurate arm", default=0)
	outfield_11 = models.BooleanField("Made someone say 'wow'", default=0)

	outfield_16 = models.BooleanField("Late jump to the ball off bat", default=0)
	outfield_17 = models.BooleanField("Angles to the ball are too short", default=0)
	outfield_18 = models.BooleanField("Feet are out of control at the catch", default=0)
	outfield_19 = models.BooleanField("In a bad position to make catch", default=0)
	outfield_20 = models.BooleanField("Proper footwork after the catch", default=0)
	outfield_21 = models.BooleanField("Difficult transfer to throwing hand", default=0)
	outfield_22 = models.BooleanField("Arm action creates loss of ball flight", default=0)
	outfield_23 = models.BooleanField("Loses momentum from catch to throw", default=0)
	outfield_24 = models.BooleanField("Weak arm", default=0)
	outfield_25 = models.BooleanField("Inaccurate arm", default=0)
	outfield_26 = models.BooleanField("Was not noticeable", default=0)

	def get_verbose_name(self):
		return self._meta.verbose_name

	def ranks(self):
		return CriterionRank.objects.filter(scoutsheet=self.id)
	
	def __unicode__(self):
		return unicode('[' + self.account.user.last_name + '] ' + self.note)
	
	class Meta:
		ordering = ['-created_date']
		verbose_name_plural = "Scout Sheets"
