# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ScoutSheet.note2'
        db.add_column(u'scout_scoutsheet', 'note2',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.note3'
        db.add_column(u'scout_scoutsheet', 'note3',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.note4'
        db.add_column(u'scout_scoutsheet', 'note4',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.dates_seen'
        db.add_column(u'scout_scoutsheet', 'dates_seen',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ab_seen'
        db.add_column(u'scout_scoutsheet', 'ab_seen',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.games_seen'
        db.add_column(u'scout_scoutsheet', 'games_seen',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.report_count'
        db.add_column(u'scout_scoutsheet', 'report_count',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.date_completed'
        db.add_column(u'scout_scoutsheet', 'date_completed',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 12, 4, 0, 0)),
                      keep_default=False)

        # Adding field 'ScoutSheet.makeup'
        db.add_column(u'scout_scoutsheet', 'makeup',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.role'
        db.add_column(u'scout_scoutsheet', 'role',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ScoutSheet.ofp'
        db.add_column(u'scout_scoutsheet', 'ofp',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


        # Changing field 'ScoutSheet.note'
        db.alter_column(u'scout_scoutsheet', 'note', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'CriterionScaleRow.column_two'
        db.alter_column(u'scout_criterionscalerow', 'column_two', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'CriterionScale.column_two_name'
        db.alter_column(u'scout_criterionscale', 'column_two_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    def backwards(self, orm):
        # Deleting field 'ScoutSheet.note2'
        db.delete_column(u'scout_scoutsheet', 'note2')

        # Deleting field 'ScoutSheet.note3'
        db.delete_column(u'scout_scoutsheet', 'note3')

        # Deleting field 'ScoutSheet.note4'
        db.delete_column(u'scout_scoutsheet', 'note4')

        # Deleting field 'ScoutSheet.dates_seen'
        db.delete_column(u'scout_scoutsheet', 'dates_seen')

        # Deleting field 'ScoutSheet.ab_seen'
        db.delete_column(u'scout_scoutsheet', 'ab_seen')

        # Deleting field 'ScoutSheet.games_seen'
        db.delete_column(u'scout_scoutsheet', 'games_seen')

        # Deleting field 'ScoutSheet.report_count'
        db.delete_column(u'scout_scoutsheet', 'report_count')

        # Deleting field 'ScoutSheet.date_completed'
        db.delete_column(u'scout_scoutsheet', 'date_completed')

        # Deleting field 'ScoutSheet.makeup'
        db.delete_column(u'scout_scoutsheet', 'makeup')

        # Deleting field 'ScoutSheet.role'
        db.delete_column(u'scout_scoutsheet', 'role')

        # Deleting field 'ScoutSheet.ofp'
        db.delete_column(u'scout_scoutsheet', 'ofp')


        # Changing field 'ScoutSheet.note'
        db.alter_column(u'scout_scoutsheet', 'note', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'CriterionScaleRow.column_two'
        db.alter_column(u'scout_criterionscalerow', 'column_two', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'CriterionScale.column_two_name'
        db.alter_column(u'scout_criterionscale', 'column_two_name', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

    models = {
        u'account.account': {
            'Meta': {'ordering': "['-created_date']", 'object_name': 'Account'},
            'college': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 12, 4, 0, 0)'}),
            'grad_year': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'high_school': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'makeup': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'note2': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'note3': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'note4': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ofp': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'report_count': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['scout']