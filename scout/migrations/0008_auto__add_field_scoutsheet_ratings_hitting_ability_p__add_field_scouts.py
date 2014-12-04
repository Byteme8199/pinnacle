# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ScoutSheet.ratings_hitting_ability_p'
        db.add_column(u'scout_scoutsheet', 'ratings_hitting_ability_p',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_hitting_ability_f'
        db.add_column(u'scout_scoutsheet', 'ratings_hitting_ability_f',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_raw_power_p'
        db.add_column(u'scout_scoutsheet', 'ratings_raw_power_p',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_raw_power_f'
        db.add_column(u'scout_scoutsheet', 'ratings_raw_power_f',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_game_power_p'
        db.add_column(u'scout_scoutsheet', 'ratings_game_power_p',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_game_power_f'
        db.add_column(u'scout_scoutsheet', 'ratings_game_power_f',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_running_speed_p'
        db.add_column(u'scout_scoutsheet', 'ratings_running_speed_p',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_running_speed_f'
        db.add_column(u'scout_scoutsheet', 'ratings_running_speed_f',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_base_running_p'
        db.add_column(u'scout_scoutsheet', 'ratings_base_running_p',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_base_running_f'
        db.add_column(u'scout_scoutsheet', 'ratings_base_running_f',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_arm_strength_p'
        db.add_column(u'scout_scoutsheet', 'ratings_arm_strength_p',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_arm_accuracy_f'
        db.add_column(u'scout_scoutsheet', 'ratings_arm_accuracy_f',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_fielding_p'
        db.add_column(u'scout_scoutsheet', 'ratings_fielding_p',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_fielding_f'
        db.add_column(u'scout_scoutsheet', 'ratings_fielding_f',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_range_p'
        db.add_column(u'scout_scoutsheet', 'ratings_range_p',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ratings_range_f'
        db.add_column(u'scout_scoutsheet', 'ratings_range_f',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.hit_type'
        db.add_column(u'scout_scoutsheet', 'hit_type',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.hit_approach'
        db.add_column(u'scout_scoutsheet', 'hit_approach',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.time_to_1b'
        db.add_column(u'scout_scoutsheet', 'time_to_1b',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.time_to_right'
        db.add_column(u'scout_scoutsheet', 'time_to_right',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.makeup_athleticism'
        db.add_column(u'scout_scoutsheet', 'makeup_athleticism',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.makeup_aptitude'
        db.add_column(u'scout_scoutsheet', 'makeup_aptitude',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.makeup_character'
        db.add_column(u'scout_scoutsheet', 'makeup_character',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.makeup_dedication'
        db.add_column(u'scout_scoutsheet', 'makeup_dedication',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.makeup_instinct'
        db.add_column(u'scout_scoutsheet', 'makeup_instinct',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.makeup_aggresiveness'
        db.add_column(u'scout_scoutsheet', 'makeup_aggresiveness',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.makeup_confidence'
        db.add_column(u'scout_scoutsheet', 'makeup_confidence',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.makeup_maturity'
        db.add_column(u'scout_scoutsheet', 'makeup_maturity',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.makeup_competitiveness'
        db.add_column(u'scout_scoutsheet', 'makeup_competitiveness',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ScoutSheet.ratings_hitting_ability_p'
        db.delete_column(u'scout_scoutsheet', 'ratings_hitting_ability_p')

        # Deleting field 'ScoutSheet.ratings_hitting_ability_f'
        db.delete_column(u'scout_scoutsheet', 'ratings_hitting_ability_f')

        # Deleting field 'ScoutSheet.ratings_raw_power_p'
        db.delete_column(u'scout_scoutsheet', 'ratings_raw_power_p')

        # Deleting field 'ScoutSheet.ratings_raw_power_f'
        db.delete_column(u'scout_scoutsheet', 'ratings_raw_power_f')

        # Deleting field 'ScoutSheet.ratings_game_power_p'
        db.delete_column(u'scout_scoutsheet', 'ratings_game_power_p')

        # Deleting field 'ScoutSheet.ratings_game_power_f'
        db.delete_column(u'scout_scoutsheet', 'ratings_game_power_f')

        # Deleting field 'ScoutSheet.ratings_running_speed_p'
        db.delete_column(u'scout_scoutsheet', 'ratings_running_speed_p')

        # Deleting field 'ScoutSheet.ratings_running_speed_f'
        db.delete_column(u'scout_scoutsheet', 'ratings_running_speed_f')

        # Deleting field 'ScoutSheet.ratings_base_running_p'
        db.delete_column(u'scout_scoutsheet', 'ratings_base_running_p')

        # Deleting field 'ScoutSheet.ratings_base_running_f'
        db.delete_column(u'scout_scoutsheet', 'ratings_base_running_f')

        # Deleting field 'ScoutSheet.ratings_arm_strength_p'
        db.delete_column(u'scout_scoutsheet', 'ratings_arm_strength_p')

        # Deleting field 'ScoutSheet.ratings_arm_accuracy_f'
        db.delete_column(u'scout_scoutsheet', 'ratings_arm_accuracy_f')

        # Deleting field 'ScoutSheet.ratings_fielding_p'
        db.delete_column(u'scout_scoutsheet', 'ratings_fielding_p')

        # Deleting field 'ScoutSheet.ratings_fielding_f'
        db.delete_column(u'scout_scoutsheet', 'ratings_fielding_f')

        # Deleting field 'ScoutSheet.ratings_range_p'
        db.delete_column(u'scout_scoutsheet', 'ratings_range_p')

        # Deleting field 'ScoutSheet.ratings_range_f'
        db.delete_column(u'scout_scoutsheet', 'ratings_range_f')

        # Deleting field 'ScoutSheet.hit_type'
        db.delete_column(u'scout_scoutsheet', 'hit_type')

        # Deleting field 'ScoutSheet.hit_approach'
        db.delete_column(u'scout_scoutsheet', 'hit_approach')

        # Deleting field 'ScoutSheet.time_to_1b'
        db.delete_column(u'scout_scoutsheet', 'time_to_1b')

        # Deleting field 'ScoutSheet.time_to_right'
        db.delete_column(u'scout_scoutsheet', 'time_to_right')

        # Deleting field 'ScoutSheet.makeup_athleticism'
        db.delete_column(u'scout_scoutsheet', 'makeup_athleticism')

        # Deleting field 'ScoutSheet.makeup_aptitude'
        db.delete_column(u'scout_scoutsheet', 'makeup_aptitude')

        # Deleting field 'ScoutSheet.makeup_character'
        db.delete_column(u'scout_scoutsheet', 'makeup_character')

        # Deleting field 'ScoutSheet.makeup_dedication'
        db.delete_column(u'scout_scoutsheet', 'makeup_dedication')

        # Deleting field 'ScoutSheet.makeup_instinct'
        db.delete_column(u'scout_scoutsheet', 'makeup_instinct')

        # Deleting field 'ScoutSheet.makeup_aggresiveness'
        db.delete_column(u'scout_scoutsheet', 'makeup_aggresiveness')

        # Deleting field 'ScoutSheet.makeup_confidence'
        db.delete_column(u'scout_scoutsheet', 'makeup_confidence')

        # Deleting field 'ScoutSheet.makeup_maturity'
        db.delete_column(u'scout_scoutsheet', 'makeup_maturity')

        # Deleting field 'ScoutSheet.makeup_competitiveness'
        db.delete_column(u'scout_scoutsheet', 'makeup_competitiveness')


    models = {
        u'account.account': {
            'Meta': {'ordering': "['-created_date']", 'object_name': 'Account'},
            'bats': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'club': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'college': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 12, 4, 0, 0)'}),
            'dob': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'eligible': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'grad_class': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'grad_year': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'high_school': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 12, 4, 0, 0)'}),
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
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 12, 4, 0, 0)'}),
            'date_completed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 12, 4, 0, 0)'}),
            'dates_seen': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'games_seen': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'hit_approach': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'hit_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'makeup': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'makeup_aggresiveness': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
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
            'ratings_arm_strength_p': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_base_running_f': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_base_running_p': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_fielding_f': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_fielding_p': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_game_power_f': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_game_power_p': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_hitting_ability_f': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_hitting_ability_p': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_range_f': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_range_p': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_raw_power_f': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_raw_power_p': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_running_speed_f': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ratings_running_speed_p': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'report_count': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'scout': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'time_to_1b': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'time_to_right': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['scout']