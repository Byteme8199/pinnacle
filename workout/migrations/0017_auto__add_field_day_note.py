# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Day.note'
        db.add_column(u'workout_day', 'note',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Day.note'
        db.delete_column(u'workout_day', 'note')


    models = {
        u'account.account': {
            'Meta': {'ordering': "['-created_date']", 'object_name': 'Account'},
            'college': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 10, 4, 0, 0)'}),
            'grad_year': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'high_school': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
        u'workout.day': {
            'Meta': {'ordering': "['due_date']", 'object_name': 'Day'},
            'due_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 10, 4, 0, 0)'}),
            'exercise_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workout.ExerciseSetGroup']"}),
            'has_completed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'routine': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workout.Routine']"})
        },
        u'workout.exerciseset': {
            'Meta': {'object_name': 'ExerciseSet'},
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workout.ExerciseType']"}),
            'exercise_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workout.ExerciseSetGroup']"}),
            'has_completed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructions': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'minutes': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'rep_info': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'reps': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'rest_minutes': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'rest_seconds': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'result': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'seconds': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'set_number': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '4'}),
            'tempo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'workout.exercisesetgroup': {
            'Meta': {'object_name': 'ExerciseSetGroup'},
            'exercise_sets': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'ExerciseSet'", 'symmetrical': 'False', 'to': u"orm['workout.ExerciseSet']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'workout.exercisetype': {
            'Meta': {'object_name': 'ExerciseType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'hints': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'workout.routine': {
            'Meta': {'object_name': 'Routine'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Account']"}),
            'created_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 10, 4, 0, 0)'}),
            'days': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'Day'", 'symmetrical': 'False', 'to': u"orm['workout.Day']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'has_completed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['workout']