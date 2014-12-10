# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ScoutSheet.ratings_fb_velocity_p'
        db.add_column(u'scout_scoutsheet', 'ratings_fb_velocity_p',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_fb_velocity_f'
        db.add_column(u'scout_scoutsheet', 'ratings_fb_velocity_f',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_fb_velocity_h'
        db.add_column(u'scout_scoutsheet', 'ratings_fb_velocity_h',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_fb_velocity_l'
        db.add_column(u'scout_scoutsheet', 'ratings_fb_velocity_l',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_fb_velocity_pc'
        db.add_column(u'scout_scoutsheet', 'ratings_fb_velocity_pc',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_fb_velocity_fc'
        db.add_column(u'scout_scoutsheet', 'ratings_fb_velocity_fc',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_fb_movement_p'
        db.add_column(u'scout_scoutsheet', 'ratings_fb_movement_p',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_fb_movement_f'
        db.add_column(u'scout_scoutsheet', 'ratings_fb_movement_f',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_fb_movement_n'
        db.add_column(u'scout_scoutsheet', 'ratings_fb_movement_n',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_curve_p'
        db.add_column(u'scout_scoutsheet', 'ratings_curve_p',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_curve_f'
        db.add_column(u'scout_scoutsheet', 'ratings_curve_f',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_curve_h'
        db.add_column(u'scout_scoutsheet', 'ratings_curve_h',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_curve_l'
        db.add_column(u'scout_scoutsheet', 'ratings_curve_l',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_curve_pc'
        db.add_column(u'scout_scoutsheet', 'ratings_curve_pc',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_curve_fc'
        db.add_column(u'scout_scoutsheet', 'ratings_curve_fc',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_slider_p'
        db.add_column(u'scout_scoutsheet', 'ratings_slider_p',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_slider_f'
        db.add_column(u'scout_scoutsheet', 'ratings_slider_f',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_slider_h'
        db.add_column(u'scout_scoutsheet', 'ratings_slider_h',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_slider_l'
        db.add_column(u'scout_scoutsheet', 'ratings_slider_l',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_slider_pc'
        db.add_column(u'scout_scoutsheet', 'ratings_slider_pc',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_slider_fc'
        db.add_column(u'scout_scoutsheet', 'ratings_slider_fc',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_change_p'
        db.add_column(u'scout_scoutsheet', 'ratings_change_p',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_change_f'
        db.add_column(u'scout_scoutsheet', 'ratings_change_f',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_change_h'
        db.add_column(u'scout_scoutsheet', 'ratings_change_h',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_change_l'
        db.add_column(u'scout_scoutsheet', 'ratings_change_l',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_change_pc'
        db.add_column(u'scout_scoutsheet', 'ratings_change_pc',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_change_fc'
        db.add_column(u'scout_scoutsheet', 'ratings_change_fc',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_other_p'
        db.add_column(u'scout_scoutsheet', 'ratings_other_p',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_other_f'
        db.add_column(u'scout_scoutsheet', 'ratings_other_f',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_other_h'
        db.add_column(u'scout_scoutsheet', 'ratings_other_h',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_other_l'
        db.add_column(u'scout_scoutsheet', 'ratings_other_l',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_other_pc'
        db.add_column(u'scout_scoutsheet', 'ratings_other_pc',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_other_fc'
        db.add_column(u'scout_scoutsheet', 'ratings_other_fc',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_control_p'
        db.add_column(u'scout_scoutsheet', 'ratings_control_p',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_control_f'
        db.add_column(u'scout_scoutsheet', 'ratings_control_f',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_pitchability_p'
        db.add_column(u'scout_scoutsheet', 'ratings_pitchability_p',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_pitchability_f'
        db.add_column(u'scout_scoutsheet', 'ratings_pitchability_f',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_delivery_p'
        db.add_column(u'scout_scoutsheet', 'ratings_delivery_p',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_delivery_f'
        db.add_column(u'scout_scoutsheet', 'ratings_delivery_f',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_arm_action_p'
        db.add_column(u'scout_scoutsheet', 'ratings_arm_action_p',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_arm_action_f'
        db.add_column(u'scout_scoutsheet', 'ratings_arm_action_f',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.delivery'
        db.add_column(u'scout_scoutsheet', 'delivery',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.arm_action'
        db.add_column(u'scout_scoutsheet', 'arm_action',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.arm_slot'
        db.add_column(u'scout_scoutsheet', 'arm_slot',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ScoutSheet.ratings_fb_velocity_p'
        db.delete_column(u'scout_scoutsheet', 'ratings_fb_velocity_p')

        # Deleting field 'ScoutSheet.ratings_fb_velocity_f'
        db.delete_column(u'scout_scoutsheet', 'ratings_fb_velocity_f')

        # Deleting field 'ScoutSheet.ratings_fb_velocity_h'
        db.delete_column(u'scout_scoutsheet', 'ratings_fb_velocity_h')

        # Deleting field 'ScoutSheet.ratings_fb_velocity_l'
        db.delete_column(u'scout_scoutsheet', 'ratings_fb_velocity_l')

        # Deleting field 'ScoutSheet.ratings_fb_velocity_pc'
        db.delete_column(u'scout_scoutsheet', 'ratings_fb_velocity_pc')

        # Deleting field 'ScoutSheet.ratings_fb_velocity_fc'
        db.delete_column(u'scout_scoutsheet', 'ratings_fb_velocity_fc')

        # Deleting field 'ScoutSheet.ratings_fb_movement_p'
        db.delete_column(u'scout_scoutsheet', 'ratings_fb_movement_p')

        # Deleting field 'ScoutSheet.ratings_fb_movement_f'
        db.delete_column(u'scout_scoutsheet', 'ratings_fb_movement_f')

        # Deleting field 'ScoutSheet.ratings_fb_movement_n'
        db.delete_column(u'scout_scoutsheet', 'ratings_fb_movement_n')

        # Deleting field 'ScoutSheet.ratings_curve_p'
        db.delete_column(u'scout_scoutsheet', 'ratings_curve_p')

        # Deleting field 'ScoutSheet.ratings_curve_f'
        db.delete_column(u'scout_scoutsheet', 'ratings_curve_f')

        # Deleting field 'ScoutSheet.ratings_curve_h'
        db.delete_column(u'scout_scoutsheet', 'ratings_curve_h')

        # Deleting field 'ScoutSheet.ratings_curve_l'
        db.delete_column(u'scout_scoutsheet', 'ratings_curve_l')

        # Deleting field 'ScoutSheet.ratings_curve_pc'
        db.delete_column(u'scout_scoutsheet', 'ratings_curve_pc')

        # Deleting field 'ScoutSheet.ratings_curve_fc'
        db.delete_column(u'scout_scoutsheet', 'ratings_curve_fc')

        # Deleting field 'ScoutSheet.ratings_slider_p'
        db.delete_column(u'scout_scoutsheet', 'ratings_slider_p')

        # Deleting field 'ScoutSheet.ratings_slider_f'
        db.delete_column(u'scout_scoutsheet', 'ratings_slider_f')

        # Deleting field 'ScoutSheet.ratings_slider_h'
        db.delete_column(u'scout_scoutsheet', 'ratings_slider_h')

        # Deleting field 'ScoutSheet.ratings_slider_l'
        db.delete_column(u'scout_scoutsheet', 'ratings_slider_l')

        # Deleting field 'ScoutSheet.ratings_slider_pc'
        db.delete_column(u'scout_scoutsheet', 'ratings_slider_pc')

        # Deleting field 'ScoutSheet.ratings_slider_fc'
        db.delete_column(u'scout_scoutsheet', 'ratings_slider_fc')

        # Deleting field 'ScoutSheet.ratings_change_p'
        db.delete_column(u'scout_scoutsheet', 'ratings_change_p')

        # Deleting field 'ScoutSheet.ratings_change_f'
        db.delete_column(u'scout_scoutsheet', 'ratings_change_f')

        # Deleting field 'ScoutSheet.ratings_change_h'
        db.delete_column(u'scout_scoutsheet', 'ratings_change_h')

        # Deleting field 'ScoutSheet.ratings_change_l'
        db.delete_column(u'scout_scoutsheet', 'ratings_change_l')

        # Deleting field 'ScoutSheet.ratings_change_pc'
        db.delete_column(u'scout_scoutsheet', 'ratings_change_pc')

        # Deleting field 'ScoutSheet.ratings_change_fc'
        db.delete_column(u'scout_scoutsheet', 'ratings_change_fc')

        # Deleting field 'ScoutSheet.ratings_other_p'
        db.delete_column(u'scout_scoutsheet', 'ratings_other_p')

        # Deleting field 'ScoutSheet.ratings_other_f'
        db.delete_column(u'scout_scoutsheet', 'ratings_other_f')

        # Deleting field 'ScoutSheet.ratings_other_h'
        db.delete_column(u'scout_scoutsheet', 'ratings_other_h')

        # Deleting field 'ScoutSheet.ratings_other_l'
        db.delete_column(u'scout_scoutsheet', 'ratings_other_l')

        # Deleting field 'ScoutSheet.ratings_other_pc'
        db.delete_column(u'scout_scoutsheet', 'ratings_other_pc')

        # Deleting field 'ScoutSheet.ratings_other_fc'
        db.delete_column(u'scout_scoutsheet', 'ratings_other_fc')

        # Deleting field 'ScoutSheet.ratings_control_p'
        db.delete_column(u'scout_scoutsheet', 'ratings_control_p')

        # Deleting field 'ScoutSheet.ratings_control_f'
        db.delete_column(u'scout_scoutsheet', 'ratings_control_f')

        # Deleting field 'ScoutSheet.ratings_pitchability_p'
        db.delete_column(u'scout_scoutsheet', 'ratings_pitchability_p')

        # Deleting field 'ScoutSheet.ratings_pitchability_f'
        db.delete_column(u'scout_scoutsheet', 'ratings_pitchability_f')

        # Deleting field 'ScoutSheet.ratings_delivery_p'
        db.delete_column(u'scout_scoutsheet', 'ratings_delivery_p')

        # Deleting field 'ScoutSheet.ratings_delivery_f'
        db.delete_column(u'scout_scoutsheet', 'ratings_delivery_f')

        # Deleting field 'ScoutSheet.ratings_arm_action_p'
        db.delete_column(u'scout_scoutsheet', 'ratings_arm_action_p')

        # Deleting field 'ScoutSheet.ratings_arm_action_f'
        db.delete_column(u'scout_scoutsheet', 'ratings_arm_action_f')

        # Deleting field 'ScoutSheet.delivery'
        db.delete_column(u'scout_scoutsheet', 'delivery')

        # Deleting field 'ScoutSheet.arm_action'
        db.delete_column(u'scout_scoutsheet', 'arm_action')

        # Deleting field 'ScoutSheet.arm_slot'
        db.delete_column(u'scout_scoutsheet', 'arm_slot')


    models = {
        u'account.account': {
            'Meta': {'ordering': "['-created_date']", 'object_name': 'Account'},
            'bats': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'club': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'college': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 12, 10, 0, 0)'}),
            'dob': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'eligible': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'grad_class': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'grad_year': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'high_school': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'team_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'throws': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'account'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'scout.criterion': {
            'Meta': {'ordering': "['name']", 'object_name': 'Criterion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'scout.criterionrank': {
            'Meta': {'ordering': "['-created_date']", 'object_name': 'CriterionRank'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 12, 10, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rank': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'scale': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scout.CriterionScale']"}),
            'scoutsheet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scout.ScoutSheet']"})
        },
        u'scout.criterionscale': {
            'Meta': {'object_name': 'CriterionScale'},
            'column_one_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'column_two_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'scout.criterionscalerow': {
            'Meta': {'ordering': "['rank']", 'object_name': 'CriterionScaleRow'},
            'column_one': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'column_two': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rank': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'scale': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scout.CriterionScale']"})
        },
        u'scout.scoutsheet': {
            'Meta': {'ordering': "['-created_date']", 'object_name': 'ScoutSheet'},
            'ab_seen': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Account']"}),
            'arm_action': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'arm_slot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 12, 10, 0, 0)'}),
            'date_completed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 12, 10, 0, 0)'}),
            'dates_seen': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'delivery': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'games_seen': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'hit_approach': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'hit_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'makeup': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'makeup_aggressiveness': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'makeup_aptitude': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'makeup_athleticism': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'makeup_character': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'makeup_competitiveness': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'makeup_confidence': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'makeup_dedication': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'makeup_instinct': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'makeup_maturity': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'note2': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'note3': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'note4': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ofp': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ratings_arm_accuracy_f': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_arm_accuracy_p': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_arm_action_f': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_arm_action_p': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_arm_strength_f': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_arm_strength_p': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_base_running_f': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_base_running_p': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_change_f': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_change_fc': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_change_h': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_change_l': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_change_p': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_change_pc': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_control_f': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_control_p': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_curve_f': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_curve_fc': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_curve_h': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_curve_l': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_curve_p': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_curve_pc': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_delivery_f': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_delivery_p': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_fb_movement_f': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_fb_movement_n': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ratings_fb_movement_p': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_fb_velocity_f': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_fb_velocity_fc': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_fb_velocity_h': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_fb_velocity_l': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_fb_velocity_p': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_fb_velocity_pc': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_fielding_f': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_fielding_p': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_game_power_f': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_game_power_p': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_hitting_ability_f': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_hitting_ability_p': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_other_f': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_other_fc': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_other_h': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_other_l': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_other_p': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_other_pc': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_pitchability_f': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_pitchability_p': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_range_f': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_range_p': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_raw_power_f': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_raw_power_p': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_running_speed_f': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_running_speed_p': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_slider_f': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_slider_fc': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_slider_h': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_slider_l': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_slider_p': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_slider_pc': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'report_count': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'scout': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'time_to_1b': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'time_to_right': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['scout']